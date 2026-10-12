import numpy as np
import onnx
import onnxruntime as ort
from PIL import Image


def preprocess(image_path):
    """将图片转换为模型所需的灰度输入格式。"""
    input_shape = (1, 1, 64, 64)
    image = Image.open(image_path).convert("L")
    image = image.resize((64, 64), Image.ANTIALIAS)
    image_data = np.array(image, dtype=np.float32)
    image_data = np.expand_dims(image_data, axis=0)
    image_data = np.expand_dims(image_data, axis=1)
    assert image_data.shape == input_shape, (
        f"Expected shape {input_shape}, but got {image_data.shape}"
    )
    return image_data


# 定义情感类别与数字标签的映射表 3分
emotion_table = #填充

# 加载 ONNX 模型 3分
ort_session = #填充

# 加载本地图片并进行预处理 3分
input_data = #填充

# 构造模型输入
ort_inputs = {ort_session.get_inputs()[0].name: input_data}

# 运行模型进行预测 3分
ort_outs = #填充

# 找到预测概率最高的情感类别 3分
predicted_label = #填充

# 根据标签获取对应情感名称 3分
predicted_emotion = #填充

print(f"Predicted emotion: {predicted_emotion}")

