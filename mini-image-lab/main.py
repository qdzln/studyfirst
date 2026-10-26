"""图像处理项目的主程序入口。"""

from pathlib import Path

from PIL import Image
from src.file_utils import list_images
from src.image_ops import average_brightness, to_grayscale
from src.report import save_report

# 当前项目的根目录
BASE_DIR = Path(__file__).resolve().parent

# 输入与输出路径
INPUT_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "outputs"


def main() -> None:
    """运行完整的图像处理流程。"""

    # 第一步：创建输入和输出目录
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 第二步：读取所有待处理图片
    image_paths = list_images(INPUT_DIR)

    if not image_paths:
        print("未找到图片，请先生成示例数据。")
        return

    # 保存每张图片的统计信息
    records = []

    # 第三步：逐张处理图片
    for image_path in image_paths:
        print(f"正在处理: {image_path.name}")

        try:
            with Image.open(image_path) as image:
                # 获取图片宽度和高度
                width, height = image.size

                # 转换成灰度图
                gray_image = to_grayscale(image)

                # 计算平均亮度
                brightness = average_brightness(gray_image)

                # 设置输出文件名
                output_path = OUTPUT_DIR / f"{image_path.stem}_gray.png"

                # 保存处理后的图片
                gray_image.save(output_path)

        except OSError as error:
            print(f"处理失败: {image_path.name}")
            print(f"错误信息: {error}")
            continue

        # 第四步：记录统计结果
        records.append(
            {
                "filename": image_path.name,
                "width": width,
                "height": height,
                "mean_brightness": round(brightness, 2),
            }
        )

        print(f"处理完成: {image_path.name}")

    # 第五步：保存 CSV 报告
    if records:
        report_path = OUTPUT_DIR / "report.csv"

        save_report(records, report_path)

        print("全部图片处理完成！")
        print(f"结果保存在: {OUTPUT_DIR}")
    else:
        print("没有成功处理的图片。")


if __name__ == "__main__":
    main()
