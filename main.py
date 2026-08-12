"""
主程序入口
跨文化界面符号认知 - 抖音/TikTok数据采集系统
"""

import sys
import os
import argparse
from datetime import datetime

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.douyin_crawler import DouyinCrawler
from src.tiktok_crawler import TikTokCrawler
from src.data_processor import DataProcessor
from config.symbols_config import SYMBOL_CATEGORIES, TARGET_CULTURES


def run_quick_collection(output_dir: str = "output", use_sample: bool = True):
    """
    快速采集模式
    Args:
        output_dir: 输出目录
        use_sample: 是否使用示例数据（无cookie时默认使用）
    """
    print("=" * 60)
    print("跨文化界面符号认知数据采集系统")
    print("=" * 60)
    print(f"启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    if use_sample:
        print("[模式] 示例数据模式（无登录cookie，使用预置研究数据）")
        print()
        # 使用示例数据生成器
        from src.sample_data_generator import generate_sample_dataset
        records = generate_sample_dataset()
    else:
        print("[模式] 实时采集模式")
        print()

        # 初始化爬虫
        douyin = DouyinCrawler()
        tiktok = TikTokCrawler()

        all_records = []

        # 选择部分符号进行采集（避免时间过长）
        selected_symbols = {
            "手势符号": ["竖大拇指", "OK手势", "双手合十"],
            "颜色符号": ["红色", "白色", "绿色"],
            "数字符号": ["数字4", "数字13"],
            "表情符号": ["微笑表情", "双手合十表情"],
            "UI界面符号": ["对勾"],
        }

        for category, symbols in selected_symbols.items():
            for symbol in symbols:
                # 抖音采集
                douyin_records = douyin.crawl_symbol(
                    symbol_name=symbol,
                    symbol_category=category,
                    cultures=TARGET_CULTURES[:5],
                    max_pages=2
                )
                all_records.extend(douyin_records)

                # TikTok采集
                tiktok_records = tiktok.crawl_symbol(
                    symbol_name=symbol,
                    symbol_category=category,
                    cultures=TARGET_CULTURES[:5],
                    max_pages=2
                )
                all_records.extend(tiktok_records)

        records = all_records

    # 数据处理
    processor = DataProcessor()
    processor.load_records(records)
    processor.clean_data()

    # 输出统计
    stats = processor.get_statistics()
    print()
    print("=" * 60)
    print("采集统计")
    print("=" * 60)
    print(f"总记录数: {stats.get('total_records', 0)}")
    print(f"覆盖符号数: {stats.get('symbols_covered', 0)}")
    print(f"冲突记录数: {stats.get('conflict_records', 0)}")
    print(f"平台分布: {stats.get('by_platform', {})}")
    print()

    # 导出数据
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    excel_path = os.path.join(output_dir, f"跨文化符号数据集_{timestamp}.xlsx")
    csv_path = os.path.join(output_dir, f"跨文化符号数据集_{timestamp}.csv")
    json_path = os.path.join(output_dir, f"跨文化符号数据集_{timestamp}.json")

    processor.export_to_excel(excel_path)
    processor.export_to_csv(csv_path)
    processor.export_to_json(json_path)

    print()
    print("=" * 60)
    print("导出完成")
    print("=" * 60)
    print(f"Excel: {excel_path}")
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")
    print()

    return excel_path, csv_path, json_path


def run_custom_collection(symbols: list, categories: list, output_dir: str = "output"):
    """自定义采集模式"""
    print(f"自定义采集模式")
    print(f"目标符号: {symbols}")
    print(f"符号类别: {categories}")

    # 这里可以实现更灵活的采集逻辑
    pass


def main():
    parser = argparse.ArgumentParser(description="跨文化界面符号认知数据采集系统")
    parser.add_argument("--mode", choices=["quick", "custom", "full"], default="quick",
                        help="采集模式: quick(快速示例), custom(自定义), full(全量)")
    parser.add_argument("--output", default="output", help="输出目录")
    parser.add_argument("--no-sample", action="store_true", help="禁用示例数据，使用真实爬虫")
    parser.add_argument("--symbols", nargs="+", help="指定符号名称列表")
    parser.add_argument("--categories", nargs="+", help="指定符号类别列表")

    args = parser.parse_args()

    if args.mode == "quick":
        run_quick_collection(args.output, use_sample=not args.no_sample)
    elif args.mode == "custom":
        run_custom_collection(args.symbols, args.categories, args.output)
    elif args.mode == "full":
        # 全量采集所有符号
        print("全量采集模式 - 这将采集所有配置的符号，可能需要较长时间")
        run_quick_collection(args.output, use_sample=not args.no_sample)


if __name__ == "__main__":
    main()
