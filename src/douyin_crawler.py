"""
抖音（国内版）爬虫模块
支持通过抖音网页版搜索接口采集跨文化符号相关视频内容
合规说明：仅采集公开可见内容，遵守平台robots协议，控制请求频率
"""

import time
import random
import hashlib
import json
import re
from datetime import datetime
from typing import List, Dict, Optional
import requests
from urllib.parse import quote

from config.symbols_config import DOUYIN_CONFIG, DOUYIN_KEYWORD_TEMPLATES


class DouyinCrawler:
    """抖音爬虫类"""

    def __init__(self, cookie: str = None, use_api: bool = False):
        """
        初始化抖音爬虫
        Args:
            cookie: 抖音登录后的cookie字符串（可选，用于获取更多数据）
            use_api: 是否使用API模式（需要cookie），默认使用网页解析模式
        """
        self.config = DOUYIN_CONFIG
        self.session = requests.Session()
        self.use_api = use_api
        self.cookie = cookie

        # 设置请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Referer": "https://www.douyin.com/",
        }
        if cookie:
            self.headers["Cookie"] = cookie

        self.session.headers.update(self.headers)
        self.collected_records = []

    def _generate_record_id(self, url: str, title: str) -> str:
        """生成唯一记录ID"""
        raw = f"{url}_{title}_{datetime.now().timestamp()}"
        return hashlib.md5(raw.encode()).hexdigest()[:16]

    def _delay(self):
        """随机延迟，避免触发反爬"""
        delay = random.uniform(*self.config["request_delay"])
        time.sleep(delay)

    def build_search_keywords(self, symbol_name: str) -> List[str]:
        """
        构建搜索关键词列表
        Args:
            symbol_name: 符号名称
        Returns:
            关键词列表
        """
        keywords = []
        for template in DOUYIN_KEYWORD_TEMPLATES:
            keyword = template.format(symbol=symbol_name)
            keywords.append(keyword)
        return keywords

    def search_videos(self, keyword: str, max_pages: int = 3) -> List[Dict]:
        """
        搜索抖音视频
        Args:
            keyword: 搜索关键词
            max_pages: 最大爬取页数
        Returns:
            视频信息列表
        """
        videos = []

        if self.use_api and self.cookie:
            videos = self._search_via_api(keyword, max_pages)
        else:
            videos = self._search_via_web(keyword, max_pages)

        return videos

    def _search_via_api(self, keyword: str, max_pages: int) -> List[Dict]:
        """通过API接口搜索（需要登录cookie）"""
        videos = []
        encoded_keyword = quote(keyword)

        for page in range(max_pages):
            try:
                params = {
                    "keyword": keyword,
                    "offset": page * 10,
                    "count": 10,
                    "search_channel": "aweme_general",
                    "sort_type": 0,
                    "publish_time": 0,
                }

                response = self.session.get(
                    self.config["api_url"],
                    params=params,
                    timeout=self.config["timeout"]
                )

                if response.status_code == 200:
                    data = response.json()
                    items = data.get("data", []).get("items", [])
                    for item in items:
                        aweme = item.get("aweme_info", {})
                        video_info = self._parse_api_video(aweme)
                        if video_info:
                            videos.append(video_info)

                self._delay()

            except Exception as e:
                print(f"[抖音API] 第{page+1}页请求失败: {e}")
                continue

        return videos

    def _search_via_web(self, keyword: str, max_pages: int) -> List[Dict]:
        """通过网页解析搜索（无需登录，数据量较少）"""
        videos = []
        encoded_keyword = quote(keyword)
        search_url = f"{self.config['search_url']}{encoded_keyword}"

        try:
            response = self.session.get(
                search_url,
                timeout=self.config["timeout"]
            )

            if response.status_code == 200:
                # 从页面HTML中提取SSR数据
                videos = self._parse_web_page(response.text)

        except Exception as e:
            print(f"[抖音网页] 搜索失败: {e}")

        return videos

    def _parse_api_video(self, aweme: Dict) -> Optional[Dict]:
        """解析API返回的视频信息"""
        try:
            aweme_id = aweme.get("aweme_id", "")
            desc = aweme.get("desc", "")
            author = aweme.get("author", {})

            # 时间戳转换
            create_time = aweme.get("create_time", 0)
            publish_time = datetime.fromtimestamp(create_time).strftime("%Y-%m-%d") if create_time else ""

            # 统计数据
            statistics = aweme.get("statistics", {})

            return {
                "aweme_id": aweme_id,
                "title": desc[:50] if desc else "",
                "desc": desc,
                "author_name": author.get("nickname", ""),
                "author_id": author.get("uid", "")[:8] + "****" if author.get("uid") else "",
                "publish_time": publish_time,
                "source_url": f"https://www.douyin.com/video/{aweme_id}",
                "like_count": statistics.get("digg_count", 0),
                "comment_count": statistics.get("comment_count", 0),
                "share_count": statistics.get("share_count", 0),
                "view_count": statistics.get("play_count", 0),
            }
        except Exception as e:
            print(f"[抖音解析] 视频信息解析失败: {e}")
            return None

    def _parse_web_page(self, html: str) -> List[Dict]:
        """解析网页HTML中的视频数据"""
        videos = []
        # 尝试从SSR数据中提取
        pattern = r'<script id="RENDER_DATA" type="application/json">(.*?)</script>'
        match = re.search(pattern, html)

        if match:
            try:
                import urllib.parse
                json_str = urllib.parse.unquote(match.group(1))
                data = json.loads(json_str)
                # 解析搜索结果数据结构
                search_data = data.get("search", {}).get("general", {}).get("data", [])
                for item in search_data:
                    aweme = item.get("aweme_info", {})
                    video_info = self._parse_api_video(aweme)
                    if video_info:
                        videos.append(video_info)
            except Exception as e:
                print(f"[抖音网页解析] 数据提取失败: {e}")

        return videos

    def crawl_symbol(self, symbol_name: str, symbol_category: str,
                     cultures: List[str] = None, max_pages: int = 3) -> List[Dict]:
        """
        采集单个符号的相关视频
        Args:
            symbol_name: 符号名称
            symbol_category: 符号类别
            cultures: 目标文化圈列表
            max_pages: 每个关键词最大页数
        Returns:
            标准化记录列表
        """
        records = []
        keywords = self.build_search_keywords(symbol_name)

        print(f"[抖音] 开始采集符号: {symbol_name} ({symbol_category})")
        print(f"[抖音] 关键词数量: {len(keywords)}")

        for i, keyword in enumerate(keywords):
            print(f"[抖音] 正在搜索 ({i+1}/{len(keywords)}): {keyword}")

            videos = self.search_videos(keyword, max_pages)

            for video in videos:
                record = self._standardize_record(
                    video, symbol_name, symbol_category, cultures
                )
                if record:
                    records.append(record)

            self._delay()

        # 去重
        records = self._deduplicate(records)
        print(f"[抖音] 符号 {symbol_name} 采集完成，共 {len(records)} 条有效记录")

        self.collected_records.extend(records)
        return records

    def _standardize_record(self, video: Dict, symbol_name: str,
                            symbol_category: str, cultures: List[str] = None) -> Optional[Dict]:
        """将视频信息标准化为统一记录格式"""
        try:
            record_id = self._generate_record_id(
                video.get("source_url", ""),
                video.get("title", "")
            )

            # 简单的文化含义提取（基于关键词匹配）
            desc = video.get("desc", "")
            cultural_meaning = self._extract_cultural_meaning(desc, symbol_name)
            potential_conflict = self._detect_conflict(desc, symbol_name)

            # 情感分析（简单规则）
            sentiment = self._analyze_sentiment(desc)

            return {
                "record_id": record_id,
                "symbol_name": symbol_name,
                "symbol_category": symbol_category,
                "culture_region": ",".join(cultures) if cultures else "全球",
                "content_title": video.get("title", ""),
                "content_desc": video.get("desc", ""),
                "author_name": video.get("author_name", ""),
                "author_id": video.get("author_id", ""),
                "publish_time": video.get("publish_time", ""),
                "collect_time": datetime.now().strftime("%Y-%m-%d"),
                "source_platform": self.config["platform_name"],
                "source_url": video.get("source_url", ""),
                "like_count": video.get("like_count", 0),
                "comment_count": video.get("comment_count", 0),
                "share_count": video.get("share_count", 0),
                "view_count": video.get("view_count", 0),
                "sentiment": sentiment,
                "cultural_meaning": cultural_meaning,
                "potential_conflict": potential_conflict,
                "optimization_suggestion": self._generate_suggestion(symbol_name, potential_conflict),
                "confidence_level": "中" if cultural_meaning else "低",
                "tags": self._extract_tags(desc)
            }
        except Exception as e:
            print(f"[抖音标准化] 记录标准化失败: {e}")
            return None

    def _extract_cultural_meaning(self, text: str, symbol: str) -> str:
        """从文本中提取文化含义"""
        # 简单的关键词匹配提取
        meaning_patterns = [
            r'在(.{2,10})代表(.{2,20})',
            r'(.{2,10})人认为(.{2,20})',
            r'象征(.{2,20})',
            r'寓意(.{2,20})',
            r'含义是(.{2,20})',
        ]

        meanings = []
        for pattern in meaning_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    meanings.append("".join(match))
                else:
                    meanings.append(match)

        return "；".join(meanings[:3]) if meanings else ""

    def _detect_conflict(self, text: str, symbol: str) -> str:
        """检测潜在的文化冲突"""
        conflict_keywords = ["禁忌", "冒犯", "不礼貌", "侮辱", "忌讳", "差异", "不同", "相反"]
        found_conflicts = [kw for kw in conflict_keywords if kw in text]

        if found_conflicts:
            return f"检测到潜在冲突关键词: {', '.join(found_conflicts)}"
        return ""

    def _analyze_sentiment(self, text: str) -> str:
        """简单情感分析"""
        positive_words = ["喜欢", "好", "棒", "赞", "美", "吉祥", "幸运", "祝福"]
        negative_words = ["讨厌", "坏", "差", "禁忌", "冒犯", "不吉利", "倒霉"]

        pos_count = sum(1 for w in positive_words if w in text)
        neg_count = sum(1 for w in negative_words if w in text)

        if pos_count > neg_count:
            return "正面"
        elif neg_count > pos_count:
            return "负面"
        else:
            return "中性"

    def _generate_suggestion(self, symbol: str, conflict: str) -> str:
        """生成优化建议"""
        if conflict:
            return f"建议在跨文化界面中谨慎使用「{symbol}」，需根据目标用户文化背景进行本地化适配"
        return f"「{symbol}」在当前采集内容中未发现明显冲突，可考虑通用化使用"

    def _extract_tags(self, text: str) -> str:
        """提取标签"""
        tags = re.findall(r'#(\S+)', text)
        return ",".join(tags[:5]) if tags else ""

    def _deduplicate(self, records: List[Dict]) -> List[Dict]:
        """基于URL和标题去重"""
        seen = set()
        unique_records = []

        for record in records:
            key = f"{record.get('source_url', '')}_{record.get('content_title', '')}"
            if key not in seen:
                seen.add(key)
                unique_records.append(record)

        return unique_records

    def get_all_records(self) -> List[Dict]:
        """获取所有采集的记录"""
        return self.collected_records
