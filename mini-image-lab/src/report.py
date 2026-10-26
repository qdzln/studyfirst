"""保存图像处理结果和统计报告"""

import csv
from pathlib import Path


def save_report(records: list[dict[str, str | int | float]], output_path: Path) -> None:
    """将图像处理结果保存为CSV报告"""
    # 确保输出目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)
    columns = ["filename", "width", "height", "mean_brightness"]
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)
