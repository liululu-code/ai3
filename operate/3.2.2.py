import numpy as np
import onnxruntime
from PIL import Image

# 加载 ONNX 模型 2分
ort_session = #填充

# 加载图片并转换为灰度图 2分
image = #填充

# 将图片调整为 MNIST 模型输入尺寸 2分
image = #填充

# 将图片转换为 float32 类型的 NumPy 数组 2分
image_array = #填充

# 添加 batch 维度 2分
image_array = #填充

# 添加通道维度 2分
image_array = #填充

# 构造模型输入 2分
ort_inputs = #填充

# 执行预测 2分
ort_outs = #填充

# 获取预测类别 2分
predicted_class = #填充

print(f"Predicted class: {predicted_class}")

