import matplotlib.pyplot as plt
import numpy as np
import pandas

# 从本地文件读取数据 2分
data = #填充
print("数据采集完成，已加载到DataFrame中")

# 打印前五条记录 2分
print #填充

# 删除缺失值 2分
data = #填充

# 转换字段数据类型 各2分
data["Age"] = #填充
data["PurchaseAmount"] = #填充
data["ReviewScore"] = #填充

# 删除不合理数据 2分
data = #填充

# 标准化购买金额和评分 各2分
data["PurchaseAmount"] = #填充
data["ReviewScore"] = #填充

# 保存清洗后的数据 1分
cleaned_file_path = "cleaned_user_behavior_data.csv"
#填充
print("数据清洗完成，已保存为 'cleaned_user_behavior_data.csv'")

# 统计每个购买类别的用户数 2分
purchase_category_counts = #填充
print("每个购买类别的用户数:\n", purchase_category_counts)

# 统计不同性别的平均购买金额 2分
gender_purchase_amount_mean = #填充
print("不同性别的平均购买金额:\n", gender_purchase_amount_mean)

# 定义年龄区间和标签
bins = [18, 26, 36, 46, 56, 66, np.inf]
labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "65+"]

# 统计不同年龄段的用户数 2分
data["AgeGroup"] = #填充
age_group_counts = #填充
print("不同年龄段的用户数:\n", age_group_counts)

