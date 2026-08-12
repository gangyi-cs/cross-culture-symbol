"""
数据处理与导出模块
支持数据清洗、去重、统计分析，以及多格式导出（Excel/CSV/JSON）
"""

import pandas as pd
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional
from collections import Counter

from config.symbols_config import OUTPUT_FIELDS


class DataProcessor:
    """数据处理器"""

    def __init__(self):
        self.records = []
        self.df = None

    def load_records(self, records: List[Dict]):
        """加载记录"""
        self.records = records
        self.df = pd.DataFrame(records)
        print(f"[数据处理] 加载 {len(records)} 条记录")

    def clean_data(self) -> pd.DataFrame:
        """数据清洗"""
        if self.df is None or self.df.empty:
            print("[数据处理] 无数据可清洗")
            return pd.DataFrame()

        df = self.df.copy()

        # 去除空标题记录
        df = df[df["content_title"].notna() & (df["content_title"] != "")]

        # 去除重复URL
        df = df.drop_duplicates(subset=["source_url"], keep="first")

        # 统一时间格式
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.strftime("%Y-%m-%d")
        df["collect_time"] = pd.to_datetime(df["collect_time"], errors="coerce").dt.strftime("%Y-%m-%d")

        # 填充缺失值
        df["cultural_meaning"] = df["cultural_meaning"].fillna("")
        df["potential_conflict"] = df["potential_conflict"].fillna("")
        df["optimization_suggestion"] = df["optimization_suggestion"].fillna("")

        # 确保所有字段存在
        for field in OUTPUT_FIELDS:
            if field not in df.columns:
                df[field] = ""

        # 按字段顺序排列
        df = df[OUTPUT_FIELDS]

        self.df = df
        print(f"[数据处理] 清洗完成，剩余 {len(df)} 条有效记录")
        return df

    def get_statistics(self) -> Dict:
        """获取统计信息"""
        if self.df is None or self.df.empty:
            return {}

        stats = {
            "total_records": len(self.df),
            "by_platform": self.df["source_platform"].value_counts().to_dict(),
            "by_category": self.df["symbol_category"].value_counts().to_dict(),
            "by_sentiment": self.df["sentiment"].value_counts().to_dict(),
            "by_confidence": self.df["confidence_level"].value_counts().to_dict(),
            "symbols_covered": self.df["symbol_name"].nunique(),
            "conflict_records": len(self.df[self.df["potential_conflict"] != ""]),
            "date_range": {
                "earliest": self.df["publish_time"].min(),
                "latest": self.df["publish_time"].max()
            },
            "top_symbols": self.df["symbol_name"].value_counts().head(10).to_dict()
        }

        return stats

    def get_conflict_analysis(self) -> pd.DataFrame:
        """获取冲突分析结果"""
        if self.df is None or self.df.empty:
            return pd.DataFrame()

        conflict_df = self.df[self.df["potential_conflict"] != ""].copy()
        return conflict_df[[
            "symbol_name", "symbol_category", "culture_region",
            "content_title", "cultural_meaning", "potential_conflict",
            "optimization_suggestion", "source_platform", "source_url"
        ]]

    def export_to_excel(self, filepath: str, include_stats: bool = True) -> str:
        """
        导出为Excel（多Sheet）
        Args:
            filepath: 输出文件路径
            include_stats: 是否包含统计Sheet
        Returns:
            文件路径
        """
        if self.df is None or self.df.empty:
            print("[数据处理] 无数据可导出")
            return ""

        with pd.ExcelWriter(filepath, engine="openpyxl") as writer:
            # 主数据表
            self.df.to_excel(writer, sheet_name="符号认知数据", index=False)

            # 冲突识别表
            conflict_df = self.get_conflict_analysis()
            if not conflict_df.empty:
                conflict_df.to_excel(writer, sheet_name="跨文化冲突识别", index=False)

            if include_stats:
                # 类别统计表
                category_stats = self.df.groupby("symbol_category").agg({
                    "record_id": "count",
                    "symbol_name": "nunique",
                    "like_count": "sum",
                    "view_count": "sum"
                }).rename(columns={
                    "record_id": "记录数",
                    "symbol_name": "符号数",
                    "like_count": "总点赞",
                    "view_count": "总播放"
                }).reset_index()
                category_stats.to_excel(writer, sheet_name="类别统计", index=False)

                # 平台分布表
                platform_stats = self.df.groupby("source_platform").agg({
                    "record_id": "count",
                    "symbol_name": "nunique",
                    "like_count": ["sum", "mean"],
                    "comment_count": "sum"
                }).reset_index()
                platform_stats.columns = ["来源平台", "记录数", "符号数", "总点赞", "平均点赞", "总评论"]
                platform_stats.to_excel(writer, sheet_name="平台分布", index=False)

                # 数据说明
                stats = self.get_statistics()
                info_data = [
                    ["项目名称", "跨文化界面符号认知数据集"],
                    ["数据来源", "抖音、TikTok"],
                    ["采集时间", datetime.now().strftime("%Y-%m-%d")],
                    ["总记录数", stats.get("total_records", 0)],
                    ["覆盖符号数", stats.get("symbols_covered", 0)],
                    ["冲突记录数", stats.get("conflict_records", 0)],
                    ["数据用途", "学术研究、跨文化界面设计参考"],
                    ["合规说明", "仅采集公开可见内容，已脱敏处理"],
                ]
                pd.DataFrame(info_data, columns=["项目", "内容"]).to_excel(
                    writer, sheet_name="数据集说明", index=False
                )

        print(f"[数据处理] Excel导出完成: {filepath}")
        return filepath

    def export_to_csv(self, filepath: str) -> str:
        """导出为CSV"""
        if self.df is None or self.df.empty:
            return ""

        self.df.to_csv(filepath, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)
        print(f"[数据处理] CSV导出完成: {filepath}")
        return filepath

    def export_to_json(self, filepath: str) -> str:
        """导出为JSON"""
        if self.df is None or self.df.empty:
            return ""

        data = {
            "metadata": {
                "project": "跨文化界面符号认知数据集",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_records": len(self.df),
                "sources": ["抖音", "TikTok"]
            },
            "records": self.df.to_dict("records")
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"[数据处理] JSON导出完成: {filepath}")
        return filepath

    def merge_records(self, *record_lists: List[Dict]) -> List[Dict]:
        """合并多个来源的记录"""
        merged = []
        for records in record_lists:
            merged.extend(records)

        # 全局去重
        seen = set()
        unique = []
        for r in merged:
            key = f"{r.get('source_url', '')}_{r.get('content_title', '')}"
            if key not in seen:
                seen.add(key)
                unique.append(r)

        self.load_records(unique)
        return unique
