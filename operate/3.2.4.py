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


# 加载模型 2分
session = #填充

# 加载类别标签 2分
with open("labels.txt") as file:
    labels = #填充

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

# 获取识别分类后的概率 2分
accuracy = #填充

# 获取预测类别索引 2分
predicted_idx = #填充

# 获取预测准确值并转换为百分比 2分
prob_percentage = #填充

# 获取预测类别标签 2分
predicted_label = #填充

print(f"Predicted class: {predicted_label}, Accuracy: {prob_percentage:.2f}%")

