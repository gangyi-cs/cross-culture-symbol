"""
跨文化界面符号配置文件
定义需要采集的符号类别、具体符号、目标文化圈
"""

# 符号类别与具体符号
SYMBOL_CATEGORIES = {
    "手势符号": [
        "竖大拇指", "OK手势", "比心手势", "剪刀手", "竖中指",
        "招手", "双手合十", "拳头", "食指指人", "摇手"
    ],
    "颜色符号": [
        "红色", "白色", "黑色", "黄色", "绿色", "蓝色",
        "紫色", "橙色", "金色", "灰色"
    ],
    "数字符号": [
        "数字4", "数字7", "数字8", "数字13", "数字6",
        "数字9", "数字0", "数字3"
    ],
    "动物符号": [
        "龙", "猫头鹰", "黑猫", "狗", "猫", "孔雀",
        "蝙蝠", "狐狸", "狮子", "蛇"
    ],
    "表情符号": [
        "微笑表情", "笑哭表情", "双手合十表情", "比心表情",
        "点赞表情", "OK手势表情", "祈祷表情", "爱心表情",
        "火焰表情", "骷髅表情"
    ],
    "UI界面符号": [
        "对勾", "叉号", "问号", "感叹号", "设置齿轮",
        "汉堡菜单", "搜索放大镜", "分享图标", "收藏星标", "下载箭头"
    ],
    "宗教文化符号": [
        "十字", "星月", "万字纹", "太极", "莲花",
        "法轮", "大卫之星", " Om符号", "生命之树", "法蒂玛之手"
    ],
    "日常物品符号": [
        "雨伞", "鞋子", "帽子", "筷子", "刀叉",
        "时钟", "镜子", "扇子", "灯笼", "风筝"
    ]
}

# 目标文化圈
TARGET_CULTURES = [
    "中国大陆", "中国香港", "中国台湾",
    "日本", "韩国",
    "美国", "英国", "法国", "德国", "意大利", "西班牙",
    "俄罗斯",
    "印度", "泰国", "越南", "印度尼西亚", "马来西亚", "菲律宾",
    "沙特阿拉伯", "阿联酋", "土耳其", "伊朗", "埃及",
    "巴西", "墨西哥", "阿根廷",
    "澳大利亚", "新西兰",
    "尼日利亚", "南非", "肯尼亚"
]

# 抖音搜索关键词模板
DOUYIN_KEYWORD_TEMPLATES = [
    "{symbol}在不同国家的含义",
    "{symbol}文化差异",
    "{symbol}外国人怎么看",
    "{symbol}在国外的意思",
    "跨文化{symbol}",
    "{symbol}禁忌",
    "{symbol}寓意",
    "{symbol}象征意义"
]

# TikTok搜索关键词模板
TIKTOK_KEYWORD_TEMPLATES = [
    "{symbol} meaning in different cultures",
    "{symbol} cultural differences",
    "what does {symbol} mean in other countries",
    "{symbol} around the world",
    "cultural {symbol}",
    "{symbol} taboo",
    "{symbol} symbolism",
    "{symbol} in different countries"
]

# 抖音平台配置
DOUYIN_CONFIG = {
    "base_url": "https://www.douyin.com",
    "search_url": "https://www.douyin.com/search/",
    "api_url": "https://www.douyin.com/aweme/v1/web/search/item/",
    "platform_name": "抖音",
    "region": "CN",
    "language": "zh-CN",
    "request_delay": (2, 5),  # 请求延迟范围（秒）
    "max_retries": 3,
    "timeout": 30
}

# TikTok平台配置
TIKTOK_CONFIG = {
    "base_url": "https://www.tiktok.com",
    "search_url": "https://www.tiktok.com/search?q=",
    "api_url": "https://www.tiktok.com/api/search/general/full/",
    "platform_name": "TikTok",
    "region": "Global",
    "language": "en",
    "request_delay": (3, 7),
    "max_retries": 3,
    "timeout": 30
}

# 输出字段定义
OUTPUT_FIELDS = [
    "record_id",           # 记录唯一ID
    "symbol_name",         # 符号名称
    "symbol_category",     # 符号类别
    "culture_region",      # 文化圈/地区
    "content_title",       # 视频/内容标题
    "content_desc",        # 内容描述/文案
    "author_name",         # 作者名称
    "author_id",           # 作者ID（脱敏）
    "publish_time",        # 发布时间
    "collect_time",        # 采集时间
    "source_platform",     # 来源平台（抖音/TikTok）
    "source_url",          # 原文链接
    "like_count",          # 点赞数
    "comment_count",       # 评论数
    "share_count",         # 分享数
    "view_count",          # 播放数
    "sentiment",           # 情感倾向（正面/中性/负面）
    "cultural_meaning",    # 提取的文化含义
    "potential_conflict",  # 潜在认知冲突
    "optimization_suggestion",  # 优化建议
    "confidence_level",    # 信息置信度
    "tags"                 # 标签
]
