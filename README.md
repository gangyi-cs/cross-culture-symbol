# 跨文化界面符号认知数据采集系统

## 项目简介
本项目是"跨文化界面符号认知壁垒研究"课题的数据采集子系统，专门用于从抖音（国内版）和TikTok（海外版）采集用户对不同文化符号的认知、解读和使用反馈，构建多文化界面符号认知数据集。

## 功能特性
- 支持抖音国内版数据采集
- 支持TikTok海外版数据采集
- 覆盖8大符号类别、80+具体符号
- 支持30+文化圈/地区
- 自动提取文化含义、检测认知冲突
- 情感倾向分析
- 数据去重、清洗、标准化
- 多格式导出（Excel/CSV/JSON）
- 飞书在线表格数据仓库同步

## 项目结构
```
douyin_tiktok_crawler/
├── main.py                    # 主程序入口
├── requirements.txt           # 依赖包
├── README.md                  # 项目说明
├── config/
│   └── symbols_config.py      # 符号配置、平台配置
├── src/
│   ├── douyin_crawler.py      # 抖音爬虫模块
│   ├── tiktok_crawler.py      # TikTok爬虫模块
│   ├── data_processor.py      # 数据处理与导出
│   └── sample_data_generator.py  # 示例数据生成器
├── data/                      # 原始数据存储
├── output/                    # 导出文件目录
└── docs/                      # 文档目录
```

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 快速运行（示例数据模式）
```bash
python main.py --mode quick
```
无需登录cookie，使用基于公开研究知识构建的示例数据集。

### 3. 真实采集模式
```bash
# 需要提供抖音/TikTok登录cookie
python main.py --mode quick --no-sample
```

### 4. 自定义采集
```python
from src.douyin_crawler import DouyinCrawler
from src.tiktok_crawler import TikTokCrawler
from src.data_processor import DataProcessor

# 初始化爬虫
douyin = DouyinCrawler(cookie="your_douyin_cookie")
tiktok = TikTokCrawler(cookie="your_tiktok_cookie")

# 采集指定符号
records = []
records.extend(douyin.crawl_symbol("红色", "颜色符号", max_pages=3))
records.extend(tiktok.crawl_symbol("红色", "颜色符号", max_pages=3))

# 数据处理
processor = DataProcessor()
processor.load_records(records)
processor.clean_data()
processor.export_to_excel("output/result.xlsx")
```

## 数据字段说明
| 字段名 | 说明 |
|--------|------|
| record_id | 记录唯一ID |
| symbol_name | 符号名称 |
| symbol_category | 符号类别 |
| culture_region | 文化圈/地区 |
| content_title | 内容标题 |
| content_desc | 内容描述 |
| author_name | 作者名称 |
| author_id | 作者ID（脱敏） |
| publish_time | 发布时间 |
| collect_time | 采集时间 |
| source_platform | 来源平台 |
| source_url | 原文链接 |
| like_count | 点赞数 |
| comment_count | 评论数 |
| share_count | 分享数 |
| view_count | 播放数 |
| sentiment | 情感倾向 |
| cultural_meaning | 文化含义 |
| potential_conflict | 潜在认知冲突 |
| optimization_suggestion | 优化建议 |
| confidence_level | 信息置信度 |
| tags | 标签 |

## 符号类别
1. 手势符号（10个）
2. 颜色符号（10个）
3. 数字符号（8个）
4. 动物符号（10个）
5. 表情符号（10个）
6. UI界面符号（10个）
7. 宗教文化符号（10个）
8. 日常物品符号（10个）

## 合规说明
- 本工具仅用于学术研究目的
- 仅采集平台公开可见的内容
- 已对用户ID等敏感信息进行脱敏处理
- 请遵守各平台的robots协议和使用条款
- 控制请求频率，避免对平台造成压力
- 建议优先使用平台官方开放API

## 注意事项
1. 抖音和TikTok都有较严格的反爬机制，真实采集建议使用官方API
2. 登录cookie具有时效性，需要定期更新
3. 海外平台采集需要确保网络环境合规
4. 采集的数据仅供学术研究使用，不得用于商业用途

## 在线数据仓库
项目数据已同步至飞书在线表格，可在线查看和协作：
- 数据仓库地址：[见项目交付文档]
- 支持在线筛选、排序、统计分析
- 可导出为多种格式

## 许可证
本项目仅供学术研究使用。
