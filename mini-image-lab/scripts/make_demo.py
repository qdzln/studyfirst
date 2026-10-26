"""生成用于测试的图像"""

from pathlib import Path

from PIL import Image

# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "raw"


def main() -> None:
    """生成测试图像"""
    # 创建目录
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    # 生成测试图像
    # 文件名与对应的的颜色RGB颜色
    examples = {"dark.png": (40, 70, 100), "bright.png": (200, 200, 200)}
    for filename, color in examples.items():
        image = Image.new("RGB", (160, 120), color)
        image.save(DATA_DIR / filename)
        print("示例图片生成完后！")


if __name__ == "__main__":
    main()
