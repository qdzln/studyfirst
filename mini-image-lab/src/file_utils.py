"""文件查找与管理工具。"""

from pathlib import Path

# 支持的图片格式
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}


def list_images(folder: Path) -> list[Path]:
    """查找文件夹中的全部图片。"""

    # 检查文件夹是否存在
    if not folder.is_dir():
        raise FileNotFoundError(f"文件夹不存在: {folder}")

    # 存储找到的图片路径
    image_paths = []

    # 遍历文件夹中的内容
    for path in folder.iterdir():
        # 判断是否为图片文件
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            image_paths.append(path)

    # 按文件名排序后返回
    return sorted(image_paths)
