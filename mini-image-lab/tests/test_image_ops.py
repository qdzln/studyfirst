"""测试图像处理模块中的函数。"""

import unittest

from PIL import Image
from src.image_ops import average_brightness, to_grayscale


class TestImageOps(unittest.TestCase):
    """图像处理功能测试。"""

    def test_black_image(self):
        """测试纯黑图像的平均亮度。"""

        image = Image.new("RGB", (10, 10), (0, 0, 0))

        result = average_brightness(image)

        self.assertAlmostEqual(result, 0.0)

    def test_white_image(self):
        """测试纯白图像的平均亮度。"""

        image = Image.new("RGB", (10, 10), (255, 255, 255))

        result = average_brightness(image)

        self.assertAlmostEqual(result, 255.0)

    def test_grayscale(self):
        """测试灰度图像转换。"""

        image = Image.new("RGB", (10, 10), (255, 0, 0))

        result = to_grayscale(image)

        self.assertEqual(result.mode, "L")


if __name__ == "__main__":
    unittest.main()
