# Mini Image Lab

一个基于 Python 的小型图像处理项目，用于学习 Python 多文件开发、项目结构和基本计算机视觉操作。

## 1. 项目功能

- 批量读取图像
- 将图像转换为灰度图
- 计算图像平均亮度
- 保存图像处理结果
- 导出 CSV 统计报告

## 2. 环境要求

- Python 3.10+
- NumPy
- Pillow

## 3. 安装环境

创建虚拟环境：

```powershell
py -3 -m venv .venv
```

安装依赖：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 4. 使用方法

生成测试图像：

```powershell
.\.venv\Scripts\python.exe scripts\make_demo.py
```

执行主程序：

```powershell
.\.venv\Scripts\python.exe main.py
```

也可以将自己的 JPG、PNG 或 BMP 图片放入 data/raw 文件夹，再执行主程序。

## 5. 项目结构

- main.py：程序入口
- src/file_utils.py：文件管理
- src/image_ops.py：图像处理
- src/report.py：保存统计报告
- scripts/make_demo.py：生成示例数据
- tests/：自动化测试
- data/raw/：原始图像
- outputs/：生成结果

## 6. 测试

在项目根目录执行：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 7. 后续改进

- 增加图片缩放
- 增加图像增强
- 支持批量数据预处理
- 扩展为 PyTorch 图像分类项目