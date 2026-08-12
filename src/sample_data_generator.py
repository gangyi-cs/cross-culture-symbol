"""
示例数据集生成器
基于跨文化符号学研究的公开知识，构建符合抖音/TikTok数据格式的示例数据集
用于无登录cookie时的演示和研究参考
"""

import random
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict


def generate_record_id(url: str, title: str) -> str:
    """生成记录ID"""
    raw = f"{url}_{title}_{random.random()}"
    return hashlib.md5(raw.encode()).hexdigest()[:16]


def random_date(start_year: int = 2023, end_year: int = 2026) -> str:
    """生成随机日期"""
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 8, 12)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")


def generate_sample_dataset() -> List[Dict]:
    """
    生成示例数据集
    基于跨文化符号学的公开研究知识构建
    """
    records = []

    # ==================== 手势符号 ====================

    # 竖大拇指
    records.extend([
        {
            "record_id": generate_record_id("dy_thumb1", "竖大拇指在中东竟是侮辱手势"),
            "symbol_name": "竖大拇指",
            "symbol_category": "手势符号",
            "culture_region": "中国,美国,中东,伊朗,伊拉克",
            "content_title": "竖大拇指在中东竟是侮辱手势！出国千万别乱比",
            "content_desc": "在中国和欧美，竖大拇指表示点赞、赞同、很棒。但在中东很多国家如伊朗、伊拉克，这个手势相当于竖中指，是极具侮辱性的动作。去中东旅游或做跨境产品一定要注意！#跨文化 #手势禁忌 #出国必备",
            "author_name": "文化差异研究所",
            "author_id": "user_a1b2****",
            "publish_time": "2025-11-03",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7298765432109876543",
            "like_count": 128500,
            "comment_count": 8932,
            "share_count": 15670,
            "view_count": 2340000,
            "sentiment": "中性",
            "cultural_meaning": "中国/欧美=赞同表扬；中东伊朗伊拉克=侮辱性手势",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,侮辱,差异",
            "optimization_suggestion": "建议在面向中东用户的界面中禁用竖大拇指图标，改用勾选或文字确认",
            "confidence_level": "高",
            "tags": "跨文化,手势禁忌,出国必备"
        },
        {
            "record_id": generate_record_id("tk_thumb1", "Thumbs up meaning in different cultures"),
            "symbol_name": "竖大拇指",
            "symbol_category": "手势符号",
            "culture_region": "Global,USA,Middle East,Persian Gulf",
            "content_title": "Thumbs up is NOT universal! What it means in 10 countries",
            "content_desc": "In America and Europe, thumbs up means good job, I agree. But in Iran, Iraq, and parts of the Middle East, it's the equivalent of the middle finger - extremely offensive! #culturaldifferences #traveltips #bodylanguage",
            "author_name": "CultureExplained",
            "author_id": "user_c3d4****",
            "publish_time": "2025-09-15",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@cultureexplained/video/7287654321098765432",
            "like_count": 245600,
            "comment_count": 12450,
            "share_count": 34200,
            "view_count": 5670000,
            "sentiment": "Neutral",
            "cultural_meaning": "USA/Europe = approval; Middle East/Iran = offensive insult",
            "potential_conflict": "Potential conflict detected: offensive, different, controversial",
            "optimization_suggestion": "Caution: 'thumbs up' may have cultural conflicts. Localization recommended for Middle Eastern markets.",
            "confidence_level": "高",
            "tags": "culturaldifferences,traveltips,bodylanguage"
        },
        {
            "record_id": generate_record_id("dy_thumb2", "竖大拇指在不同国家的含义"),
            "symbol_name": "竖大拇指",
            "symbol_category": "手势符号",
            "culture_region": "中国,日本,韩国,美国,澳大利亚",
            "content_title": "一个竖大拇指，在不同国家意思完全不同！",
            "content_desc": "竖大拇指在中国是表扬，在日本表示男人、老板，在澳大利亚曾经是侮辱手势现在逐渐被接受。全球化时代做产品真的要注意这些细节。#设计 #全球化 #用户体验",
            "author_name": "产品设计笔记",
            "author_id": "user_e5f6****",
            "publish_time": "2026-01-20",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7301234567890123456",
            "like_count": 45600,
            "comment_count": 2340,
            "share_count": 6780,
            "view_count": 890000,
            "sentiment": "中性",
            "cultural_meaning": "中国=表扬；日本=男人/老板；澳大利亚=曾为侮辱",
            "potential_conflict": "检测到潜在冲突关键词: 不同,差异",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「竖大拇指」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "中",
            "tags": "设计,全球化,用户体验"
        },
    ])

    # OK手势
    records.extend([
        {
            "record_id": generate_record_id("dy_ok1", "OK手势在巴西是侮辱"),
            "symbol_name": "OK手势",
            "symbol_category": "手势符号",
            "culture_region": "中国,美国,日本,法国,巴西,土耳其",
            "content_title": "OK手势千万别乱比！在这些国家是骂人",
            "content_desc": "OK手势在美国表示没问题，在日本代表金钱，在法国表示零或毫无价值，在巴西和土耳其则是侮辱性手势，类似于竖中指。做跨境电商的朋友一定要注意产品图片！#跨境电商 #文化差异 #手势",
            "author_name": "出海运营笔记",
            "author_id": "user_g7h8****",
            "publish_time": "2025-07-22",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7265432109876543210",
            "like_count": 89200,
            "comment_count": 5670,
            "share_count": 12300,
            "view_count": 1560000,
            "sentiment": "中性",
            "cultural_meaning": "美国=没问题；日本=金钱；法国=零/无价值；巴西土耳其=侮辱",
            "potential_conflict": "检测到潜在冲突关键词: 侮辱,差异,不同",
            "optimization_suggestion": "跨境公共界面建议取消纯OK手势图标，改用文字或通用符号",
            "confidence_level": "高",
            "tags": "跨境电商,文化差异,手势"
        },
        {
            "record_id": generate_record_id("tk_ok1", "OK gesture offensive in some countries"),
            "symbol_name": "OK手势",
            "symbol_category": "手势符号",
            "culture_region": "Global,USA,Japan,France,Brazil,Turkey",
            "content_title": "The OK hand sign is offensive in these countries!",
            "content_desc": "The OK gesture means 'okay' in the US, 'money' in Japan, 'zero' in France, but in Brazil and Turkey it's an insult! Be careful when traveling or designing for global audiences. #culture #design #globalization",
            "author_name": "GlobalDesignPro",
            "author_id": "user_i9j0****",
            "publish_time": "2026-03-10",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@globaldesign/video/7345678901234567890",
            "like_count": 167800,
            "comment_count": 8900,
            "share_count": 23400,
            "view_count": 3450000,
            "sentiment": "Neutral",
            "cultural_meaning": "USA=okay; Japan=money; France=zero; Brazil/Turkey=offensive",
            "potential_conflict": "Potential conflict detected: offensive, different",
            "optimization_suggestion": "Caution: 'OK gesture' may have cultural conflicts. Avoid in global UI designs.",
            "confidence_level": "高",
            "tags": "culture,design,globalization"
        },
    ])

    # 双手合十
    records.extend([
        {
            "record_id": generate_record_id("dy_fold1", "双手合十在不同文化的含义"),
            "symbol_name": "双手合十",
            "symbol_category": "手势符号",
            "culture_region": "中国,日本,泰国,印度,欧美",
            "content_title": "双手合十🙏在不同国家的真实含义",
            "content_desc": "在中国，双手合十表示拜托、感谢、祈祷。在泰国是问候礼(Sawasdee)，在印度是Namaste问候，在日本多用于道歉和感谢，在欧美基督教文化中表示祈祷。一个手势多种含义！#文化 #手势 # emoji",
            "author_name": "文化小课堂",
            "author_id": "user_k1l2****",
            "publish_time": "2025-12-05",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7312345678901234567",
            "like_count": 67800,
            "comment_count": 3450,
            "share_count": 8900,
            "view_count": 1230000,
            "sentiment": "正面",
            "cultural_meaning": "中国=拜托感谢；泰国=问候礼；印度=Namaste；日本=道歉感谢；欧美=祈祷",
            "potential_conflict": "检测到潜在冲突关键词: 不同",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「双手合十」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "高",
            "tags": "文化,手势,emoji"
        },
        {
            "record_id": generate_record_id("tk_fold1", "Folded hands emoji meaning worldwide"),
            "symbol_name": "双手合十",
            "symbol_category": "手势符号",
            "culture_region": "Global,China,Japan,Thailand,India,USA",
            "content_title": "What 🙏 actually means in different cultures",
            "content_desc": "The folded hands emoji means prayer in Western countries, but in China it means 'please' or 'thank you', in Thailand it's a greeting, in India it's Namaste, in Japan it means apology or thanks. One emoji, so many meanings! #emoji #culture #communication",
            "author_name": "EmojiExpert",
            "author_id": "user_m3n4****",
            "publish_time": "2026-02-18",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@emojiexpert/video/7334567890123456789",
            "like_count": 198700,
            "comment_count": 15600,
            "share_count": 28900,
            "view_count": 4560000,
            "sentiment": "Positive",
            "cultural_meaning": "West=prayer; China=please/thanks; Thailand=greeting; India=Namaste; Japan=apology",
            "potential_conflict": "Potential conflict detected: different",
            "optimization_suggestion": "Caution: 'folded hands' may have cultural conflicts. Context-dependent interpretation needed.",
            "confidence_level": "高",
            "tags": "emoji,culture,communication"
        },
    ])

    # ==================== 颜色符号 ====================

    # 红色
    records.extend([
        {
            "record_id": generate_record_id("dy_red1", "红色在不同文化的含义"),
            "symbol_name": "红色",
            "symbol_category": "颜色符号",
            "culture_region": "中国,欧美,印度,中东,南非",
            "content_title": "红色在中国是喜庆，在国外竟是这个意思！",
            "content_desc": "红色在中国象征喜庆、吉祥、繁荣，春节结婚都用红色。但在欧美红色常代表危险、警告、停止。在印度红色代表纯洁和婚姻，在中东部分地区红色象征邪恶和警告。做全球化设计颜色真的很重要！#设计 #颜色 #全球化",
            "author_name": "UI设计灵感",
            "author_id": "user_o5p6****",
            "publish_time": "2026-02-10",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7335678901234567890",
            "like_count": 56700,
            "comment_count": 2890,
            "share_count": 7800,
            "view_count": 980000,
            "sentiment": "中性",
            "cultural_meaning": "中国=喜庆吉祥；欧美=危险警告；印度=纯洁婚姻；中东=邪恶警告",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「红色」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "高",
            "tags": "设计,颜色,全球化"
        },
        {
            "record_id": generate_record_id("tk_red1", "Red color meaning in different cultures"),
            "symbol_name": "红色",
            "symbol_category": "颜色符号",
            "culture_region": "Global,China,USA,India,Middle East,Africa",
            "content_title": "Red means different things around the world!",
            "content_desc": "In China, red means luck, happiness, prosperity. In Western countries, red means danger, warning, stop. In India, red symbolizes purity and marriage. In parts of Africa, red represents death and mourning. Color matters in global design! #design #colortheory #ux",
            "author_name": "DesignWorld",
            "author_id": "user_q7r8****",
            "publish_time": "2025-10-28",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@designworld/video/7298765432109876543",
            "like_count": 134500,
            "comment_count": 7800,
            "share_count": 19800,
            "view_count": 2890000,
            "sentiment": "Neutral",
            "cultural_meaning": "China=luck/happiness; West=danger/warning; India=purity/marriage; Africa=death/mourning",
            "potential_conflict": "Potential conflict detected: different",
            "optimization_suggestion": "Caution: 'red color' may have cultural conflicts. Localization recommended for color schemes.",
            "confidence_level": "高",
            "tags": "design,colortheory,ux"
        },
    ])

    # 白色
    records.extend([
        {
            "record_id": generate_record_id("dy_white1", "白色在中西文化中的差异"),
            "symbol_name": "白色",
            "symbol_category": "颜色符号",
            "culture_region": "中国,欧美,日本,印度",
            "content_title": "白色在中国是丧事，在西方却是婚礼！",
            "content_desc": "在中国传统文化中，白色是丧葬之色，代表哀悼。但在欧美，白色象征纯洁、神圣，新娘结婚穿白色婚纱。在日本白色也有神圣和死亡的双重含义。跨文化设计中颜色选择必须谨慎！#文化差异 #设计 #颜色",
            "author_name": "文化对比研究",
            "author_id": "user_s9t0****",
            "publish_time": "2025-08-15",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7276543210987654321",
            "like_count": 78900,
            "comment_count": 4560,
            "share_count": 11200,
            "view_count": 1450000,
            "sentiment": "中性",
            "cultural_meaning": "中国传统=丧葬哀悼；欧美=纯洁神圣婚礼；日本=神圣+死亡双重含义",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「白色」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "高",
            "tags": "文化差异,设计,颜色"
        },
    ])

    # 绿色
    records.extend([
        {
            "record_id": generate_record_id("dy_green1", "绿色在伊斯兰文化中的神圣地位"),
            "symbol_name": "绿色",
            "symbol_category": "颜色符号",
            "culture_region": "中国,中东伊斯兰国家,欧美,日本",
            "content_title": "绿色在伊斯兰国家是神圣的！千万别乱用",
            "content_desc": "绿色在伊斯兰文化中是神圣的颜色，代表天堂和生命，沙特阿拉伯国旗就是绿色。但在中国，绿色有特殊含义（绿帽子），在欧美绿色代表自然、环保，也可以表示嫉妒。做中东市场的产品一定要注意绿色的使用！#中东 #伊斯兰 #设计",
            "author_name": "中东市场观察",
            "author_id": "user_u1v2****",
            "publish_time": "2026-04-22",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7356789012345678901",
            "like_count": 34500,
            "comment_count": 1890,
            "share_count": 5600,
            "view_count": 670000,
            "sentiment": "中性",
            "cultural_meaning": "伊斯兰=神圣天堂；中国=自然环保但有绿帽子负面含义；欧美=自然环保/嫉妒",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,差异",
            "optimization_suggestion": "建议在面向伊斯兰市场的界面中，绿色应保持神圣性，不宜用于普通按钮或负面提示",
            "confidence_level": "高",
            "tags": "中东,伊斯兰,设计"
        },
        {
            "record_id": generate_record_id("tk_green1", "Green color sacred in Islamic culture"),
            "symbol_name": "绿色",
            "symbol_category": "颜色符号",
            "culture_region": "Global,Middle East,Islamic countries,China,USA",
            "content_title": "Why green is sacred in Islamic culture",
            "content_desc": "Green is the most sacred color in Islam, representing paradise and life. Saudi Arabia's flag is green. But in China, green hats have a negative connotation. In the West, green means nature and environmentalism. Be careful using green in global products! #islamicdesign #middleeast #ux",
            "author_name": "MiddleEastDesign",
            "author_id": "user_w3x4****",
            "publish_time": "2025-11-30",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@medesign/video/7309876543210987654",
            "like_count": 89200,
            "comment_count": 5400,
            "share_count": 14500,
            "view_count": 1780000,
            "sentiment": "Neutral",
            "cultural_meaning": "Islamic=sacred/paradise; China=nature but negative hat connotation; West=nature/environment",
            "potential_conflict": "Potential conflict detected: different, taboo",
            "optimization_suggestion": "Caution: 'green color' may have cultural conflicts. Respect sacred connotations in Islamic markets.",
            "confidence_level": "高",
            "tags": "islamicdesign,middleeast,ux"
        },
    ])

    # ==================== 数字符号 ====================

    # 数字4
    records.extend([
        {
            "record_id": generate_record_id("dy_4_1", "数字4在东亚国家的禁忌"),
            "symbol_name": "数字4",
            "symbol_category": "数字符号",
            "culture_region": "中国,日本,韩国,欧美,东南亚",
            "content_title": "为什么电梯没有4楼？数字4的禁忌文化",
            "content_desc": "数字4在中国、日本、韩国因为谐音'死'被认为不吉利，很多建筑没有4楼、4号房。但在欧美4是完全中性的数字，在泰国4反而被认为是幸运数字。做全球化产品编号系统要注意！#数字禁忌 #文化 #设计",
            "author_name": "冷知识研究所",
            "author_id": "user_y5z6****",
            "publish_time": "2025-09-08",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7287654321098765432",
            "like_count": 156000,
            "comment_count": 9800,
            "share_count": 23400,
            "view_count": 3200000,
            "sentiment": "中性",
            "cultural_meaning": "中日韩=不吉利谐音死；欧美=中性；泰国=幸运",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,差异,不同",
            "optimization_suggestion": "东亚市场产品编号、楼层、座位号建议跳过数字4，或提供可配置选项",
            "confidence_level": "高",
            "tags": "数字禁忌,文化,设计"
        },
        {
            "record_id": generate_record_id("tk_4_1", "Number 4 unlucky in East Asia"),
            "symbol_name": "数字4",
            "symbol_category": "数字符号",
            "culture_region": "Global,China,Japan,Korea,USA,Thailand",
            "content_title": "Why there's no 4th floor in East Asian buildings",
            "content_desc": "The number 4 sounds like 'death' in Chinese, Japanese, and Korean, so it's considered unlucky. Many buildings skip the 4th floor! But in Thailand, 4 is lucky. Tetraphobia is real in East Asia. #numbers #culture #eastasia",
            "author_name": "AsianCulture101",
            "author_id": "user_a7b8****",
            "publish_time": "2026-01-15",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@asianculture/video/7323456789012345678",
            "like_count": 287600,
            "comment_count": 18900,
            "share_count": 45600,
            "view_count": 6780000,
            "sentiment": "Neutral",
            "cultural_meaning": "China/Japan/Korea=unlucky (death); West=neutral; Thailand=lucky",
            "potential_conflict": "Potential conflict detected: different, taboo",
            "optimization_suggestion": "Caution: 'number 4' may have cultural conflicts. Skip in East Asian product numbering systems.",
            "confidence_level": "高",
            "tags": "numbers,culture,eastasia"
        },
    ])

    # 数字13
    records.extend([
        {
            "record_id": generate_record_id("dy_13_1", "数字13在西方的禁忌"),
            "symbol_name": "数字13",
            "symbol_category": "数字符号",
            "culture_region": "欧美,中国,日本,印度,意大利",
            "content_title": "13号星期五为什么不吉利？西方数字禁忌",
            "content_desc": "数字13在西方文化中被认为不吉利，源于最后的晚餐有13人，很多建筑没有13楼，航空公司没有13排。但在中国13是中性甚至偏吉的数字，在意大利17才是不吉利数字。全球化产品要注意不同地区的数字禁忌！#西方文化 #数字 #禁忌",
            "author_name": "西方文化小百科",
            "author_id": "user_c9d0****",
            "publish_time": "2025-10-13",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7298765432109876543",
            "like_count": 98700,
            "comment_count": 6700,
            "share_count": 15600,
            "view_count": 1890000,
            "sentiment": "中性",
            "cultural_meaning": "欧美=不吉利最后的晚餐；中国=中性偏吉；意大利=17才不吉利",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,差异,不同",
            "optimization_suggestion": "欧美市场产品编号、楼层建议可跳过13，东亚市场则无需特别处理",
            "confidence_level": "高",
            "tags": "西方文化,数字,禁忌"
        },
    ])

    # ==================== 表情符号 ====================

    # 微笑表情
    records.extend([
        {
            "record_id": generate_record_id("dy_smile1", "微笑表情在年轻人中的含义变化"),
            "symbol_name": "微笑表情",
            "symbol_category": "表情符号",
            "culture_region": "中国,欧美,日本,韩国",
            "content_title": "😊这个表情千万别发给年轻人！已经变味了",
            "content_desc": "微笑表情😊在欧美和日本仍然表示友好、开心，但在中国年轻网民中，这个表情已经变成了讽刺、敷衍、礼貌性疏远的代名词。官方和长辈还在用，但年轻人看到会觉得被阴阳。做面向年轻用户的产品要注意！#emoji #年轻人 #社交",
            "author_name": "互联网观察",
            "author_id": "user_e1f2****",
            "publish_time": "2026-05-20",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7367890123456789012",
            "like_count": 234500,
            "comment_count": 18900,
            "share_count": 45600,
            "view_count": 4560000,
            "sentiment": "中性",
            "cultural_meaning": "欧美日本=友好开心；中国年轻人=讽刺敷衍疏远",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "面向中国年轻用户的正式政务/客服界面建议减少原生微笑表情，改用更明确的友好图标",
            "confidence_level": "高",
            "tags": "emoji,年轻人,社交"
        },
        {
            "record_id": generate_record_id("tk_smile1", "Smiling emoji means sarcasm in China"),
            "symbol_name": "微笑表情",
            "symbol_category": "表情符号",
            "culture_region": "Global,China,USA,Japan,Korea",
            "content_title": "The 😊 emoji means something different in China!",
            "content_desc": "In the West and Japan, the smiling emoji means friendly and happy. But among young Chinese internet users, it now means sarcasm, passive-aggressiveness, or being dismissive! Generational and cultural differences in emoji use are fascinating. #emoji #genz #china",
            "author_name": "InternetCulture",
            "author_id": "user_g3h4****",
            "publish_time": "2026-03-25",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@internetculture/video/7356789012345678901",
            "like_count": 345600,
            "comment_count": 23400,
            "share_count": 56700,
            "view_count": 7890000,
            "sentiment": "Neutral",
            "cultural_meaning": "West/Japan=friendly/happy; China youth=sarcasm/dismissive",
            "potential_conflict": "Potential conflict detected: different, opposite, controversial",
            "optimization_suggestion": "Caution: 'smiling emoji' may have cultural conflicts. Avoid in formal Chinese youth-facing interfaces.",
            "confidence_level": "高",
            "tags": "emoji,genz,china"
        },
    ])

    # ==================== UI界面符号 ====================

    # 对勾
    records.extend([
        {
            "record_id": generate_record_id("dy_check1", "对勾和圆圈在日本的含义差异"),
            "symbol_name": "对勾",
            "symbol_category": "UI界面符号",
            "culture_region": "中国,欧美,日本,韩国",
            "content_title": "日本人不用对勾表示正确？这个符号差异太大了",
            "content_desc": "在中国和欧美，对勾✓表示正确、通过、同意。但在日本，正确通常用圆圈○表示，对勾✓反而可能表示错误或有问题。做日本市场的产品表单、考试系统一定要注意这个差异！#日本 #UI设计 #符号",
            "author_name": "日本设计研究",
            "author_id": "user_i5j6****",
            "publish_time": "2025-12-18",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7318901234567890123",
            "like_count": 67800,
            "comment_count": 4500,
            "share_count": 12300,
            "view_count": 1230000,
            "sentiment": "中性",
            "cultural_meaning": "中国欧美=正确通过同意；日本=圆圈表示正确对勾可能表示错误",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "日本市场的表单、考试、审批界面建议使用圆圈○表示正确，对勾需配合文字说明",
            "confidence_level": "高",
            "tags": "日本,UI设计,符号"
        },
    ])

    # ==================== 动物符号 ====================

    # 龙
    records.extend([
        {
            "record_id": generate_record_id("dy_dragon1", "龙在中西文化中的巨大差异"),
            "symbol_name": "龙",
            "symbol_category": "动物符号",
            "culture_region": "中国,欧美,日本,韩国,东南亚",
            "content_title": "中国龙vs西方龙，完全是两种生物！",
            "content_desc": "龙在中国是祥瑞、权威、中华民族的象征，代表吉祥和力量。但在西方文化中，龙(dragon)通常是邪恶的怪物，代表危险和毁灭。做品牌logo和文化输出时一定要注意这个差异！#龙 #文化差异 #品牌",
            "author_name": "中华文化讲堂",
            "author_id": "user_k7l8****",
            "publish_time": "2026-02-17",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7336789012345678901",
            "like_count": 189000,
            "comment_count": 12300,
            "share_count": 34500,
            "view_count": 3450000,
            "sentiment": "正面",
            "cultural_meaning": "中国=祥瑞权威民族象征；西方=邪恶怪物危险毁灭",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "面向西方市场使用龙元素时需注意形象优化，避免被误解为邪恶象征",
            "confidence_level": "高",
            "tags": "龙,文化差异,品牌"
        },
        {
            "record_id": generate_record_id("tk_dragon1", "Dragons: East vs West completely different"),
            "symbol_name": "龙",
            "symbol_category": "动物符号",
            "culture_region": "Global,China,West,Japan,Korea",
            "content_title": "Chinese dragons vs Western dragons are NOT the same!",
            "content_desc": "In China, dragons are auspicious, powerful, symbols of the nation and good fortune. In Western culture, dragons are usually evil monsters representing danger and destruction. This cultural difference is huge for branding! #dragon #culture #branding",
            "author_name": "CultureShock",
            "author_id": "user_m9n0****",
            "publish_time": "2025-08-05",
            "collect_time": "2026-08-12",
            "source_platform": "TikTok",
            "source_url": "https://www.tiktok.com/@cultureshock/video/7265432109876543210",
            "like_count": 456700,
            "comment_count": 34500,
            "share_count": 78900,
            "view_count": 8900000,
            "sentiment": "Positive",
            "cultural_meaning": "China=auspicious/powerful/nation symbol; West=evil monster/danger",
            "potential_conflict": "Potential conflict detected: different, opposite, controversial",
            "optimization_suggestion": "Caution: 'dragon' may have cultural conflicts. Image optimization needed for Western markets.",
            "confidence_level": "高",
            "tags": "dragon,culture,branding"
        },
    ])

    # 猫头鹰
    records.extend([
        {
            "record_id": generate_record_id("dy_owl1", "猫头鹰在不同文化中的含义"),
            "symbol_name": "猫头鹰",
            "symbol_category": "动物符号",
            "culture_region": "中国,欧美,日本,印度,非洲",
            "content_title": "猫头鹰在西方是智慧象征，在中国竟是不吉利？",
            "content_desc": "猫头鹰在古希腊和西方文化中是智慧的象征，雅典娜的圣鸟就是猫头鹰。但在中国传统中，猫头鹰被认为是不祥之鸟，代表厄运和死亡。在印度部分地区也有负面含义。做教育类产品出海要注意！#猫头鹰 #文化 #教育",
            "author_name": "动物文化志",
            "author_id": "user_o1p2****",
            "publish_time": "2025-11-20",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7307654321098765432",
            "like_count": 45600,
            "comment_count": 2300,
            "share_count": 6700,
            "view_count": 780000,
            "sentiment": "中性",
            "cultural_meaning": "西方=智慧雅典娜；中国传统=不祥厄运死亡；印度部分=负面",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「猫头鹰」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "中",
            "tags": "猫头鹰,文化,教育"
        },
    ])

    # ==================== 宗教文化符号 ====================

    # 万字纹
    records.extend([
        {
            "record_id": generate_record_id("dy_swastika1", "万字纹的文化争议"),
            "symbol_name": "万字纹",
            "symbol_category": "宗教文化符号",
            "culture_region": "中国,日本,印度,欧美,全球",
            "content_title": "这个符号在佛教中是吉祥，在西方却是禁忌！",
            "content_desc": "万字纹(卍)在佛教、印度教中是吉祥万福的象征，有几千年历史。但因为纳粹德国使用了旋转45度的卐作为标志，在西方这个符号成为了禁忌和仇恨的象征。在全球化产品中使用这个符号一定要极其谨慎！#佛教 #符号 #历史",
            "author_name": "符号学研究",
            "author_id": "user_q3r4****",
            "publish_time": "2026-01-08",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7320987654321098765",
            "like_count": 78900,
            "comment_count": 8900,
            "share_count": 15600,
            "view_count": 1560000,
            "sentiment": "中性",
            "cultural_meaning": "佛教印度教=吉祥万福几千年；西方=纳粹仇恨禁忌",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,争议,差异,不同",
            "optimization_suggestion": "全球化产品中强烈建议避免使用万字纹，如必须使用需明确标注宗教语境并做地区屏蔽",
            "confidence_level": "高",
            "tags": "佛教,符号,历史"
        },
    ])

    # ==================== 日常物品符号 ====================

    # 鞋子
    records.extend([
        {
            "record_id": generate_record_id("dy_shoes1", "鞋子在中东文化中的禁忌"),
            "symbol_name": "鞋子",
            "symbol_category": "日常物品符号",
            "culture_region": "中东,中国,欧美,日本,印度",
            "content_title": "在中东千万别用脚指人！鞋子的文化禁忌",
            "content_desc": "在中东和穆斯林文化中，脚和鞋子被认为是不洁的，用脚或鞋底对着别人是极大的侮辱。进入清真寺和他人家中必须脱鞋。做中东市场的产品图片和UI设计要注意避免展示鞋底对着人的画面！#中东 #文化禁忌 #设计",
            "author_name": "跨文化沟通",
            "author_id": "user_s5t6****",
            "publish_time": "2026-04-05",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7350123456789012345",
            "like_count": 56700,
            "comment_count": 3400,
            "share_count": 8900,
            "view_count": 980000,
            "sentiment": "中性",
            "cultural_meaning": "中东穆斯林=脚和鞋不洁鞋底对人是侮辱；欧美=相对随意；日本=进屋脱鞋",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,侮辱,差异",
            "optimization_suggestion": "中东市场产品图片和UI设计应避免展示鞋底对着人的画面，尊重当地文化习俗",
            "confidence_level": "高",
            "tags": "中东,文化禁忌,设计"
        },
    ])

    # 雨伞
    records.extend([
        {
            "record_id": generate_record_id("dy_umbrella1", "室内打伞的文化禁忌"),
            "symbol_name": "雨伞",
            "symbol_category": "日常物品符号",
            "culture_region": "中国,欧美,日本,全球",
            "content_title": "室内打伞不吉利？这个迷信中外都有！",
            "content_desc": "在中国和西方都有室内打伞会带来厄运的迷信说法。在西方这个说法源于古罗马，在中国则与丧葬习俗有关。虽然是迷信，但做产品设计时如果面向保守用户群体，还是要注意避免室内撑伞的画面。#迷信 #文化 #设计",
            "author_name": "文化冷知识",
            "author_id": "user_u7v8****",
            "publish_time": "2025-07-30",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7269876543210987654",
            "like_count": 34500,
            "comment_count": 1800,
            "share_count": 5600,
            "view_count": 560000,
            "sentiment": "中性",
            "cultural_meaning": "中国西方=室内打伞带来厄运迷信；日本=也有类似说法",
            "potential_conflict": "检测到潜在冲突关键词: 禁忌,差异",
            "optimization_suggestion": "面向保守用户群体的产品设计应避免室内撑伞的画面，尊重文化迷信",
            "confidence_level": "中",
            "tags": "迷信,文化,设计"
        },
    ])

    # 补充更多记录以丰富数据集
    # 比心手势
    records.extend([
        {
            "record_id": generate_record_id("dy_heart1", "比心手势的起源和文化差异"),
            "symbol_name": "比心手势",
            "symbol_category": "手势符号",
            "culture_region": "中国,韩国,日本,欧美,东南亚",
            "content_title": "比心手势起源于韩国？在不同国家含义不同",
            "content_desc": "手指比心手势近年来在全球流行，起源于韩国K-pop文化。在中国表示爱、喜欢、支持，在欧美也逐渐被接受表示爱意。但在部分中东和保守地区，这个手势可能被误解。做社交产品要注意！#比心 #K-pop #文化",
            "author_name": "流行文化观察",
            "author_id": "user_w9x0****",
            "publish_time": "2026-06-15",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7378901234567890123",
            "like_count": 123000,
            "comment_count": 7800,
            "share_count": 19800,
            "view_count": 2340000,
            "sentiment": "正面",
            "cultural_meaning": "中韩=爱喜欢支持；欧美=逐渐接受爱意；中东保守地区=可能被误解",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「比心手势」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "中",
            "tags": "比心,K-pop,文化"
        },
    ])

    # 数字8
    records.extend([
        {
            "record_id": generate_record_id("dy_8_1", "数字8在中国的吉祥含义"),
            "symbol_name": "数字8",
            "symbol_category": "数字符号",
            "culture_region": "中国,日本,韩国,欧美,东南亚",
            "content_title": "为什么中国人这么喜欢数字8？",
            "content_desc": "数字8在中国因为谐音'发'（发财）被认为是最吉利的数字，手机号、车牌号、开业日期都抢8。但在欧美8是普通数字，在日本8也有吉祥含义但不如中国强烈。全球化产品定价和编号可以利用这个文化偏好！#数字 #中国文化 #商业",
            "author_name": "商业文化研究",
            "author_id": "user_y1z2****",
            "publish_time": "2025-10-01",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7289012345678901234",
            "like_count": 89000,
            "comment_count": 5600,
            "share_count": 12300,
            "view_count": 1670000,
            "sentiment": "正面",
            "cultural_meaning": "中国=发财最吉利；日本=也有吉祥含义；欧美=普通中性",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同",
            "optimization_suggestion": "「数字8」在当前采集内容中未发现明显冲突，中国市场可利用其吉祥含义进行定价和编号设计",
            "confidence_level": "高",
            "tags": "数字,中国文化,商业"
        },
    ])

    # 黑猫
    records.extend([
        {
            "record_id": generate_record_id("dy_cat1", "黑猫在不同文化中的含义"),
            "symbol_name": "黑猫",
            "symbol_category": "动物符号",
            "culture_region": "欧美,中国,日本,埃及,英国",
            "content_title": "黑猫是厄运还是好运？不同文化完全相反！",
            "content_desc": "在美国和西欧，黑猫被认为是不吉利的，尤其是黑猫从面前走过。但在英国和日本，黑猫反而是好运的象征。在古埃及，猫是神圣的动物。做万圣节和宠物相关产品要注意这些文化差异！#黑猫 #文化 #宠物",
            "author_name": "宠物文化志",
            "author_id": "user_a3b4****",
            "publish_time": "2025-10-31",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7300123456789012345",
            "like_count": 67000,
            "comment_count": 4500,
            "share_count": 9800,
            "view_count": 1120000,
            "sentiment": "中性",
            "cultural_meaning": "美国西欧=不吉利厄运；英国日本=好运象征；古埃及=神圣",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "建议在跨文化界面中谨慎使用「黑猫」，需根据目标用户文化背景进行本地化适配",
            "confidence_level": "高",
            "tags": "黑猫,文化,宠物"
        },
    ])

    # 剪刀手
    records.extend([
        {
            "record_id": generate_record_id("dy_v1", "剪刀手在不同国家的含义"),
            "symbol_name": "剪刀手",
            "symbol_category": "手势符号",
            "culture_region": "中国,日本,韩国,英国,澳大利亚,美国",
            "content_title": "剪刀手✌️在英国竟是侮辱手势？",
            "content_desc": "剪刀手(V字手势)在中国和亚洲是拍照必备手势，表示和平、胜利、可爱。但在英国、澳大利亚、爱尔兰等国家，如果手背朝外做V手势，是侮辱性手势（相当于竖中指）。只有手心朝外才是胜利。出国拍照要注意！#手势 #拍照 #文化",
            "author_name": "旅行文化指南",
            "author_id": "user_c5d6****",
            "publish_time": "2026-05-01",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7361234567890123456",
            "like_count": 156000,
            "comment_count": 11200,
            "share_count": 28900,
            "view_count": 2890000,
            "sentiment": "中性",
            "cultural_meaning": "亚洲=和平胜利可爱拍照；英国澳洲爱尔兰=手背朝外是侮辱",
            "potential_conflict": "检测到潜在冲突关键词: 侮辱,差异,不同",
            "optimization_suggestion": "面向英联邦国家的界面中，V字手势图标应确保手心朝外，或避免使用手势类图标",
            "confidence_level": "高",
            "tags": "手势,拍照,文化"
        },
    ])

    # 数字7
    records.extend([
        {
            "record_id": generate_record_id("dy_7_1", "数字7在不同文化中的含义"),
            "symbol_name": "数字7",
            "symbol_category": "数字符号",
            "culture_region": "欧美,中国,日本,印度,中东",
            "content_title": "数字7为什么在西方是幸运数字？",
            "content_desc": "数字7在西方文化中是幸运数字，源于基督教（上帝7天创世）和古希腊（7大行星）。赌场老虎机777就是大奖。但在中国7没有特别含义，在日本7也有吉祥含义（七夕）。在伊斯兰文化中7也很神圣。#数字 #幸运 #文化",
            "author_name": "数字文化研究",
            "author_id": "user_e7f8****",
            "publish_time": "2025-09-25",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7282345678901234567",
            "like_count": 45000,
            "comment_count": 2100,
            "share_count": 6700,
            "view_count": 780000,
            "sentiment": "正面",
            "cultural_meaning": "西方=幸运基督教创世；日本=吉祥七夕；伊斯兰=神圣；中国=中性",
            "potential_conflict": "检测到潜在冲突关键词: 差异",
            "optimization_suggestion": "「数字7」在当前采集内容中未发现明显冲突，可考虑通用化使用",
            "confidence_level": "中",
            "tags": "数字,幸运,文化"
        },
    ])

    # 叉号
    records.extend([
        {
            "record_id": generate_record_id("dy_cross1", "叉号在不同文化中的含义"),
            "symbol_name": "叉号",
            "symbol_category": "UI界面符号",
            "culture_region": "中国,欧美,日本,韩国,全球",
            "content_title": "UI设计中的叉号✕，在日本表示正确？",
            "content_desc": "在大多数国家，叉号✕表示错误、关闭、取消。但在日本的学校教育中，叉号反而表示正确（和圆圈配合使用时），这与其他国家完全相反。不过在现代UI设计中，日本也逐渐接受了叉号表示关闭的国际惯例。#UI设计 #日本 #符号",
            "author_name": "UI设计规范",
            "author_id": "user_g9h0****",
            "publish_time": "2026-03-18",
            "collect_time": "2026-08-12",
            "source_platform": "抖音",
            "source_url": "https://www.douyin.com/video/7342345678901234567",
            "like_count": 34000,
            "comment_count": 1800,
            "share_count": 5600,
            "view_count": 560000,
            "sentiment": "中性",
            "cultural_meaning": "大多数国家=错误关闭取消；日本学校=表示正确现代UI逐渐国际化",
            "potential_conflict": "检测到潜在冲突关键词: 差异,不同,相反",
            "optimization_suggestion": "日本市场的考试和教育类界面需注意叉号与圆圈的含义差异，普通UI可遵循国际惯例",
            "confidence_level": "中",
            "tags": "UI设计,日本,符号"
        },
    ])

    print(f"[示例数据生成] 共生成 {len(records)} 条记录")
    return records
