"""提供图像预处理功能"""

import numpy as np
from PIL import Image, ImageOps


def to_grayscale(image: Image.Image) -> Image.Image:
    """将图像转换为灰度图像"""
    return ImageOps.grayscale(image)


def average_brightness(image: Image.Image) -> float:
    """计算图像的平均亮度"""
    gray_image = image.convert("L")  # 转换为灰度图像
    pixels = np.array(gray_image, dtype=np.float32)  # 转换为NumPy数组
    mean_value = pixels.mean()  # 计算平均值
    return float(mean_value)  # 返回平均亮度值


def resize_image(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """调整图像尺寸"""
    return image.resize(size, Image.Resampling.LANCZOS)
