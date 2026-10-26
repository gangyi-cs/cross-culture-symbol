# 跨文化界面符号认知研究：编码本与采集工具

## 项目简介
本项目是"跨文化界面符号认知壁垒研究与适配平台研发"课题的数据基础项目，包含两部分：
1. **符号-文化释义编码本**（`examples/` 目录）：基于跨文化符号学文献与公开讨论整理的编码数据集
2. **采集工具**（`src/` 目录）：抖音/TikTok 爬虫实现（可运行，尚未接入大规模真实采集）

## ⚠️ 重要数据说明

**`examples/` 目录下的数据文件为示例编码本（Demo Coding Sheet），非大规模爬虫采集结果。**

- 数据性质：基于跨文化符号学文献、HCI实验研究、公开讨论整理的"符号—文化释义编码本"
- 规模：共 29 条示例条目，覆盖 8 大符号类别
- 字段说明：`source_url`、`author_id`、点赞数等为构造值，不代表真实爬取结果
- 爬虫模块（`src/douyin_crawler.py`、`src/tiktok_crawler.py`）为可运行实现，但尚未接入大规模真实采集
- 完整扩充版数据见飞书在线表格（86条，含文献整理+真实案例）

## 功能特性
- 抖音/TikTok 数据采集模块（可运行）
- 符号认知冲突检测与情感分析
- 多格式导出（Excel/CSV/JSON）
- 基于文献的符号-文化释义编码本

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
├── examples/                  # 示例编码本（非真实采集）
│   ├── 跨文化界面符号认知数据集_抖音TikTok.csv
│   ├── 跨文化界面符号认知数据集_抖音TikTok.json
│   └── 跨文化界面符号认知数据集_抖音TikTok.xlsx
├── docs/
│   └── REFERENCES.md           # 参考文献列表（40条）
├── data/                      # 原始数据存储（预留）
└── output/                    # 导出文件目录（预留）
```

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 查看示例编码本
```bash
# examples/ 目录下即为整理好的示例数据
# 可直接用 Excel 或 Python 读取
```

### 3. 爬虫模块（需配置cookie）
```python
from src.douyin_crawler import DouyinCrawler
from src.tiktok_crawler import TikTokCrawler

# 初始化爬虫（需要真实登录cookie）
douyin = DouyinCrawler(cookie="your_douyin_cookie")
tiktok = TikTokCrawler(cookie="your_tiktok_cookie")
```

## 数据字段说明
| 字段名 | 说明 |
|--------|------|
| record_id | 记录唯一ID |
| symbol_name | 符号名称 |
| symbol_category | 符号类别 |
| culture_region | 文化圈/地区 |
| content_title | 内容标题（整理） |
| content_desc | 内容描述（整理） |
| author_name | 来源类型（文献整理/公开讨论） |
| author_id | 作者ID（示例数据为占位符） |
| publish_time | 发布时间（示例数据为占位符） |
| collect_time | 整理时间 |
| source_platform | 来源类型（文献整理/抖音/TikTok） |
| source_url | 原文链接（示例数据为占位符） |
| like_count | 点赞数（示例数据为占位符） |
| comment_count | 评论数（示例数据为占位符） |
| share_count | 分享数（示例数据为占位符） |
| view_count | 播放数（示例数据为占位符） |
| sentiment | 情感倾向 |
| cultural_meaning | 文化含义 |
| potential_conflict | 潜在认知冲突 |
| optimization_suggestion | 优化建议 |
| confidence_level | 信息置信度 |
| tags | 标签 |

## 符号类别
1. 手势符号
2. 颜色符号
3. 数字符号
4. 动物符号
5. 表情符号
6. UI界面符号
7. 宗教文化符号
8. 日常物品符号

## 参考文献
本编码本的文化释义结论参考了以下学术研究，完整列表见 `docs/REFERENCES.md`：

1. Chen Y. et al. (2024). Individual differences in emoji comprehension. PLOS ONE. DOI: 10.1371/journal.pone.0297379
2. Brejcha J. (2015). Chinese UI Design Guidelines 2.0. DUXU, Springer LNCS. DOI: 10.1007/978-3-319-20886-2_12
3. Mongolian and Chinese Color Perception (2019). Frontiers in Psychology. DOI: 10.3389/fpsyg.2019.00551

## 合规说明
- 本项目仅用于学术研究目的
- 示例编码本基于公开文献与公开讨论整理，不涉及用户隐私
- 爬虫模块请遵守各平台的robots协议和使用条款
- 控制请求频率，避免对平台造成压力
- 建议优先使用平台官方开放API

## 在线数据仓库
完整扩充版数据（86条，含文献整理+真实案例）：
- 飞书表格地址：https://my.feishu.cn/sheets/XCgFs8o0mhzlSdtt8MUc9OpZnpb

## 许可证
本项目仅供学术研究使用。
