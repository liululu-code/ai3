import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取传感器数据集 2分
data = #填充

# 按传感器类型分组，统计数据数量和平均值 3分
sensor_stats = #填充
print("传感器数据数量和平均值:")
print(sensor_stats)

# 筛选温度和湿度数据，按位置和传感器类型统计平均值 2分
location_stats = #填充
print("每个位置的温度和湿度数据平均值:")
print(location_stats)

# 根据温度和湿度的合理范围标记异常值 3分
data["is_abnormal"] = #填充

# 输出异常值数量 2分
abnormal_count = #填充
print("异常值数量:", abnormal_count)

# 使用前向填充和后向填充处理缺失值 4分
#填充
#填充

# 删除异常值标记列 2分
cleaned_data = #填充

# 保存清洗后的数据 2分
cleaned_file_path = "cleaned_sensor_data.csv"
#填充
print("数据清洗完成，已保存为 'cleaned_sensor_data.csv'")

