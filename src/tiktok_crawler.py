"""
TikTok（海外版）爬虫模块
支持通过TikTok网页版搜索接口采集跨文化符号相关视频内容
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

from config.symbols_config import TIKTOK_CONFIG, TIKTOK_KEYWORD_TEMPLATES


class TikTokCrawler:
    """TikTok爬虫类"""

    def __init__(self, cookie: str = None, use_api: bool = False):
        """
        初始化TikTok爬虫
        Args:
            cookie: TikTok登录后的cookie字符串（可选）
            use_api: 是否使用API模式
        """
        self.config = TIKTOK_CONFIG
        self.session = requests.Session()
        self.use_api = use_api
        self.cookie = cookie

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.tiktok.com/",
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
        """随机延迟"""
        delay = random.uniform(*self.config["request_delay"])
        time.sleep(delay)

    def build_search_keywords(self, symbol_name: str) -> List[str]:
        """构建搜索关键词列表"""
        keywords = []
        # 符号名称英文映射
        symbol_en = self._translate_symbol(symbol_name)
        for template in TIKTOK_KEYWORD_TEMPLATES:
            keyword = template.format(symbol=symbol_en)
            keywords.append(keyword)
        return keywords

    def _translate_symbol(self, symbol_name: str) -> str:
        """符号名称中英文映射"""
        translation_map = {
            "竖大拇指": "thumbs up",
            "OK手势": "OK gesture",
            "比心手势": "finger heart",
            "剪刀手": "peace sign",
            "竖中指": "middle finger",
            "招手": "waving hand",
            "双手合十": "folded hands",
            "拳头": "fist",
            "食指指人": "pointing finger",
            "摇手": "shaking hand",
            "红色": "red color",
            "白色": "white color",
            "黑色": "black color",
            "黄色": "yellow color",
            "绿色": "green color",
            "蓝色": "blue color",
            "紫色": "purple color",
            "橙色": "orange color",
            "金色": "gold color",
            "灰色": "gray color",
            "数字4": "number 4",
            "数字7": "number 7",
            "数字8": "number 8",
            "数字13": "number 13",
            "数字6": "number 6",
            "数字9": "number 9",
            "数字0": "number 0",
            "数字3": "number 3",
            "龙": "dragon",
            "猫头鹰": "owl",
            "黑猫": "black cat",
            "狗": "dog",
            "猫": "cat",
            "孔雀": "peacock",
            "蝙蝠": "bat",
            "狐狸": "fox",
            "狮子": "lion",
            "蛇": "snake",
            "微笑表情": "smiling emoji",
            "笑哭表情": "laugh crying emoji",
            "双手合十表情": "praying hands emoji",
            "比心表情": "heart emoji",
            "点赞表情": "thumbs up emoji",
            "OK手势表情": "OK hand emoji",
            "祈祷表情": "prayer emoji",
            "爱心表情": "love heart",
            "火焰表情": "fire emoji",
            "骷髅表情": "skull emoji",
            "对勾": "check mark",
            "叉号": "cross mark",
            "问号": "question mark",
            "感叹号": "exclamation mark",
            "设置齿轮": "settings gear",
            "汉堡菜单": "hamburger menu",
            "搜索放大镜": "search magnifier",
            "分享图标": "share icon",
            "收藏星标": "star favorite",
            "下载箭头": "download arrow",
            "十字": "cross symbol",
            "星月": "crescent moon star",
            "万字纹": "swastika",
            "太极": "tai chi yin yang",
            "莲花": "lotus flower",
            "法轮": "dharma wheel",
            "大卫之星": "star of david",
            "Om符号": "om symbol",
            "生命之树": "tree of life",
            "法蒂玛之手": "hamsa hand",
            "雨伞": "umbrella",
            "鞋子": "shoes",
            "帽子": "hat",
            "筷子": "chopsticks",
            "刀叉": "knife fork",
            "时钟": "clock",
            "镜子": "mirror",
            "扇子": "fan",
            "灯笼": "lantern",
            "风筝": "kite"
        }
        return translation_map.get(symbol_name, symbol_name)

    def search_videos(self, keyword: str, max_pages: int = 3) -> List[Dict]:
        """搜索TikTok视频"""
        videos = []

        if self.use_api and self.cookie:
            videos = self._search_via_api(keyword, max_pages)
        else:
            videos = self._search_via_web(keyword, max_pages)

        return videos

    def _search_via_api(self, keyword: str, max_pages: int) -> List[Dict]:
        """通过API搜索"""
        videos = []

        for page in range(max_pages):
            try:
                params = {
                    "keyword": keyword,
                    "offset": page * 10,
                    "count": 10,
                }

                response = self.session.get(
                    self.config["api_url"],
                    params=params,
                    timeout=self.config["timeout"]
                )

                if response.status_code == 200:
                    data = response.json()
                    items = data.get("data", [])
                    for item in items:
                        video_info = self._parse_api_video(item)
                        if video_info:
                            videos.append(video_info)

                self._delay()

            except Exception as e:
                print(f"[TikTok API] 第{page+1}页请求失败: {e}")
                continue

        return videos

    def _search_via_web(self, keyword: str, max_pages: int) -> List[Dict]:
        """通过网页解析搜索"""
        videos = []
        encoded_keyword = quote(keyword)
        search_url = f"{self.config['search_url']}{encoded_keyword}"

        try:
            response = self.session.get(
                search_url,
                timeout=self.config["timeout"]
            )

            if response.status_code == 200:
                videos = self._parse_web_page(response.text)

        except Exception as e:
            print(f"[TikTok网页] 搜索失败: {e}")

        return videos

    def _parse_api_video(self, item: Dict) -> Optional[Dict]:
        """解析API视频信息"""
        try:
            video = item.get("video", {})
            author = item.get("author", {})
            stats = item.get("stats", {})

            create_time = item.get("createTime", 0)
            publish_time = datetime.fromtimestamp(int(create_time)).strftime("%Y-%m-%d") if create_time else ""

            return {
                "video_id": item.get("id", ""),
                "title": item.get("desc", "")[:50],
                "desc": item.get("desc", ""),
                "author_name": author.get("nickname", ""),
                "author_id": author.get("id", "")[:8] + "****" if author.get("id") else "",
                "publish_time": publish_time,
                "source_url": f"https://www.tiktok.com/@{author.get('uniqueId', '')}/video/{item.get('id', '')}",
                "like_count": stats.get("diggCount", 0),
                "comment_count": stats.get("commentCount", 0),
                "share_count": stats.get("shareCount", 0),
                "view_count": stats.get("playCount", 0),
            }
        except Exception as e:
            print(f"[TikTok解析] 视频解析失败: {e}")
            return None

    def _parse_web_page(self, html: str) -> List[Dict]:
        """解析网页HTML"""
        videos = []
        pattern = r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>'
        match = re.search(pattern, html)

        if match:
            try:
                data = json.loads(match.group(1))
                search_results = data.get("__DEFAULT_SCOPE__", {}).get("web.search.general", {})
                items = search_results.get("data", [])

                for item in items:
                    if item.get("type") == 1:  # 视频类型
                        video_info = self._parse_api_video(item.get("item", {}))
                        if video_info:
                            videos.append(video_info)
            except Exception as e:
                print(f"[TikTok网页解析] 数据提取失败: {e}")

        return videos

    def crawl_symbol(self, symbol_name: str, symbol_category: str,
                     cultures: List[str] = None, max_pages: int = 3) -> List[Dict]:
        """采集单个符号"""
        records = []
        keywords = self.build_search_keywords(symbol_name)

        print(f"[TikTok] 开始采集符号: {symbol_name} ({symbol_category})")
        print(f"[TikTok] 关键词数量: {len(keywords)}")

        for i, keyword in enumerate(keywords):
            print(f"[TikTok] 正在搜索 ({i+1}/{len(keywords)}): {keyword}")

            videos = self.search_videos(keyword, max_pages)

            for video in videos:
                record = self._standardize_record(
                    video, symbol_name, symbol_category, cultures
                )
                if record:
                    records.append(record)

            self._delay()

        records = self._deduplicate(records)
        print(f"[TikTok] 符号 {symbol_name} 采集完成，共 {len(records)} 条有效记录")

        self.collected_records.extend(records)
        return records

    def _standardize_record(self, video: Dict, symbol_name: str,
                            symbol_category: str, cultures: List[str] = None) -> Optional[Dict]:
        """标准化记录"""
        try:
            record_id = self._generate_record_id(
                video.get("source_url", ""),
                video.get("title", "")
            )

            desc = video.get("desc", "")
            cultural_meaning = self._extract_cultural_meaning(desc, symbol_name)
            potential_conflict = self._detect_conflict(desc)
            sentiment = self._analyze_sentiment(desc)

            return {
                "record_id": record_id,
                "symbol_name": symbol_name,
                "symbol_category": symbol_category,
                "culture_region": ",".join(cultures) if cultures else "Global",
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
            print(f"[TikTok标准化] 记录标准化失败: {e}")
            return None

    def _extract_cultural_meaning(self, text: str, symbol: str) -> str:
        """提取文化含义"""
        meaning_patterns = [
            r'in (.{2,20}) means (.{2,30})',
            r'(.{2,20}) people think (.{2,30})',
            r'symbolizes? (.{2,30})',
            r'represents? (.{2,30})',
            r'stands for (.{2,30})',
        ]

        meanings = []
        for pattern in meaning_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    meanings.append(" - ".join(match))
                else:
                    meanings.append(match)

        return "; ".join(meanings[:3]) if meanings else ""

    def _detect_conflict(self, text: str) -> str:
        """检测冲突"""
        conflict_keywords = ["taboo", "offensive", "rude", "insult", "different", "opposite", "controversial"]
        found = [kw for kw in conflict_keywords if kw.lower() in text.lower()]

        if found:
            return f"Potential conflict detected: {', '.join(found)}"
        return ""

    def _analyze_sentiment(self, text: str) -> str:
        """情感分析"""
        positive = ["love", "good", "great", "awesome", "beautiful", "lucky", "blessed"]
        negative = ["hate", "bad", "terrible", "taboo", "offensive", "unlucky", "cursed"]

        pos = sum(1 for w in positive if w.lower() in text.lower())
        neg = sum(1 for w in negative if w.lower() in text.lower())

        if pos > neg:
            return "Positive"
        elif neg > pos:
            return "Negative"
        else:
            return "Neutral"

    def _generate_suggestion(self, symbol: str, conflict: str) -> str:
        """生成建议"""
        if conflict:
            return f"Caution: '{symbol}' may have cultural conflicts. Localization recommended for target markets."
        return f"'{symbol}' shows no obvious conflict in collected content. General use may be acceptable."

    def _extract_tags(self, text: str) -> str:
        """提取标签"""
        tags = re.findall(r'#(\w+)', text)
        return ",".join(tags[:5]) if tags else ""

    def _deduplicate(self, records: List[Dict]) -> List[Dict]:
        """去重"""
        seen = set()
        unique = []

        for record in records:
            key = f"{record.get('source_url', '')}_{record.get('content_title', '')}"
            if key not in seen:
                seen.add(key)
                unique.append(record)

        return unique

    def get_all_records(self) -> List[Dict]:
        """获取所有记录"""
        return self.collected_records
