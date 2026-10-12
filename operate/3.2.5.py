import os
import time

import cv2
import numpy as np
import onnxruntime as ort
import vision.utils.box_utils_numpy as box_utils


def predict(
    width,
    height,
    confidences,
    boxes,
    prob_threshold,
    iou_threshold=0.3,
    top_k=-1,
):
    """对模型输出的边界框和置信度进行后处理。"""
    boxes = boxes[0]
    confidences = confidences[0]
    picked_box_probs = []
    picked_labels = []
    for class_index in range(1, confidences.shape[1]):
        probs = confidences[:, class_index]
        mask = probs > prob_threshold
        probs = probs[mask]
        if probs.shape[0] == 0:
            continue
        subset_boxes = boxes[mask, :]
        box_probs = np.concatenate([subset_boxes, probs.reshape(-1, 1)], axis=1)
        box_probs = box_utils.hard_nms(
            box_probs,
            iou_threshold=iou_threshold,
            top_k=top_k,
        )
        picked_box_probs.append(box_probs)
        picked_labels.extend([class_index] * box_probs.shape[0])
    if not picked_box_probs:
        return np.array([]), np.array([]), np.array([])
    picked_box_probs = np.concatenate(picked_box_probs)
    picked_box_probs[:, 0] *= width
    picked_box_probs[:, 1] *= height
    picked_box_probs[:, 2] *= width
    picked_box_probs[:, 3] *= height
    return (
        picked_box_probs[:, :4].astype(np.int32),
        np.array(picked_labels),
        picked_box_probs[:, 4],
    )


# 从标签文件读取类别名称 2分
class_names = #填充

# 创建 ONNX Runtime 推理会话 2分
ort_session = #填充

# 获取模型输入名称 2分
input_name = #填充

result_path = "./detect_imgs_results_onnx"
threshold = 0.7
path = "imgs"
sum = 0

# 如果结果目录不存在，则创建目录 2分
if not os.path.exists(result_path):
    #填充

listdir = os.listdir(path)
for file_path in listdir:
    img_path = os.path.join(path, file_path)

    # 使用 OpenCV 读取图片 2分
    orig_image = #填充

    # 将 BGR 图片转换为 RGB
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)

    # 将图片调整为 320x240 2分
    image = #填充

    # 定义图像归一化均值 2分
    image_mean = #填充
    image = (image - image_mean) / 128
    image = np.transpose(image, [2, 0, 1])

    # 添加 batch 维度 1分
    image = #填充
    image = image.astype(np.float32)

    start_time = time.time()

    # 使用 ONNX Runtime 执行推理 2分
    confidences, boxes = #填充
    print("cost time:{}".format(time.time() - start_time))

    boxes, labels, probs = predict(
        orig_image.shape[1],
        orig_image.shape[0],
        confidences,
        boxes,
        threshold,
    )

    for i in range(boxes.shape[0]):
        box = boxes[i, :]
        label = f"{class_names[labels[i]]}: {probs[i]:.2f}"
        cv2.rectangle(
            orig_image,
            (box[0], box[1]),
            (box[2], box[3]),
            (255, 255, 0),
            4,
        )
        cv2.imwrite(os.path.join(result_path, file_path), orig_image)

    sum += boxes.shape[0]

print("sum:{}".format(sum))
