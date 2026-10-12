import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 读取 Excel 数据集并显示前五行 1分
data = #填充
print #填充

# 处理缺失值，并统计处理前后的数据行数 2分
initial_row_count = #填充
data = #填充
final_row_count = #填充
print(f"处理后数据行数: {final_row_count}, 删除的行数: {initial_row_count - final_row_count}")

# 删除重复行 1分
data = #填充

# 对指定数值特征进行标准化处理 1分
numerical_features = #填充
scaler = #填充
data[numerical_features] = #填充

# 选择特征 1分
selected_features = #填充
X = data[selected_features]

# 创建目标变量 1分
y = #填充

# 将数据划分为训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 合并特征和目标变量 1分
cleaned_data = #填充

# 保存处理后的数据 1分
cleaned_file_path = "2.1.2_cleaned_data.csv"
#填充
