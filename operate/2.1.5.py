import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 加载数据集并查看表结构 2分
data = #填充
print #填充

# 显示每一列的缺失值数量 1分
print #填充

# 删除含有缺失值的行 1分
data_cleaned = #填充

# 将 Your age 列转换为整数类型并处理异常值 1分
data_cleaned.loc[:, "Your age"] = #填充
data_cleaned = #填充
data_cleaned = #填充
data_cleaned.loc[:, "Your age"] = #填充
print(data_cleaned["Your age"].dtype)

# 检查并删除重复值 1分
duplicates_removed = #填充
data_cleaned = #填充
print(f"Removed {duplicates_removed} duplicate rows")

# 对健身水平列进行编码处理 1分
label_encoder = #填充
data_cleaned["How do you describe your current level of fitness ?"] = #填充
print(data_cleaned["How do you describe your current level of fitness ?"].unique())

# 去掉列名两侧的空格
data.columns = data.columns.str.strip()
print(data.columns)

# 统计健身频率并绘制饼图 1分
data_cleaned = #填充
exercise_frequency_counts = #填充
plt.figure(figsize=(10, 6))
#填充
plt.title("Distribution of Exercise Frequency")
plt.ylabel("")
plt.show()

# 使用众数填充缺失值
data_filled = #填充

# 划分训练集和测试集 1分
train_data, test_data = #填充

# 保存处理后的数据 1分
cleaned_file_path = "2.1.5_cleaned_data.csv"
#填充
