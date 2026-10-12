import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 从本地文件读取数据 2分
data = #填充
print("数据采集完成，已加载到DataFrame中")

# 打印前五条记录 2分
print #填充

# 删除缺失值 2分
data = #填充

# 转换字段数据类型 各1分
data["Age"] = #填充
data["Speed"] = #填充
data["TravelDistance"] = #填充
data["TravelTime"] = #填充

# 删除不合理数据 2分
data = #填充

# 保存清洗后的数据 1分
cleaned_file_path = "cleaned_vehicle_traffic_data.csv"
#填充
print("数据清洗完成，已保存为 'cleaned_vehicle_traffic_data.csv'")

# 审核字段合理性 2分
unreasonable_data = #填充
print("不合理的数据:\n", unreasonable_data)

# 统计每种交通事件的发生次数 2分
traffic_event_counts = #填充
print("每种交通事件的发生次数:\n", traffic_event_counts)

# 统计不同性别的平均车速、行驶距离和行驶时间 2分
gender_stats = #填充
print("不同性别的平均车速、行驶距离和行驶时间:\n", gender_stats)

# 定义年龄区间和标签
age_bins = [18, 26, 36, 46, 56, 66, np.inf]
age_labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "65+"]

# 统计不同年龄段的驾驶员数 5分
data["AgeGroup"] = #填充
age_group_counts = #填充
print("不同年龄段的驾驶员数:\n", age_group_counts)
