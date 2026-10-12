import numpy as np
import onnxruntime as ort
import scipy.special
from PIL import Image


def preprocess_image(
    image,
    resize_size=256,
    crop_size=224,
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225],
):
    """将图片转换为模型要求的输入格式。"""
    image = image.resize((resize_size, resize_size), Image.BILINEAR)
    width, height = image.size
    left = (width - crop_size) / 2
    top = (height - crop_size) / 2
    image = image.crop((left, top, left + crop_size, top + crop_size))
    image = np.array(image).astype(np.float32)
    image = image / 255.0
    image = (image - mean) / std
    image = np.transpose(image, (2, 0, 1))
    image = image.reshape((1,) + image.shape)
    return image


# 加载 ONNX 模型 2分
session = #填充

# 加载类别标签
labels_path = "labels.txt"
with open(labels_path) as file:
    labels = [line.strip() for line in file.readlines()]

# 获取模型输入和输出名称
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

# 加载图片 2分
image = #填充

# 预处理图片 2分
processed_image = #填充
processed_image = processed_image.astype(np.float32)

# 使用模型识别图片 2分
output = #填充

# 使用 softmax 获取分类概率 2分
probabilities = #填充

# 获取最高的五个概率及类别索引 3分
top5_idx = #填充
top5_prob = #填充

print("Top 5 predicted classes:")
for i in range(5):
    print(f"{i + 1}: {labels[top5_idx[i]]} - Probability: {top5_prob[i]}")

