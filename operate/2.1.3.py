import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# 加载数据并显示前五行 1分
data = #填充
print #填充

# 识别数值列并绘制箱线图，辅助观察异常值
numeric_cols = data.select_dtypes(include=["float64", "int64"]).columns
plt.figure(figsize=(12, 8))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 4, i)
    sns.boxplot(x=data[col])
    plt.title(col)
plt.tight_layout()
plt.show()

# 使用 IQR 方法识别并移除异常值 2分
Q1 = #填充
Q3 = #填充
IQR = #填充
data_cleaned = #填充

# 检查并删除重复值 1分
duplicates = #填充
num_duplicates = #填充
data_cleaned = #填充
print(f"删除的重复行数: {num_duplicates}")

# 对数值型数据进行归一化处理 1分
scaler = #填充
data_cleaned[numeric_cols] = #填充

# 设置目标变量 1分
target_variable = #填充

# 定义特征和目标变量 2分
X = #填充
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充
print(f"训练数据形状: {X_train.shape}")
print(f"测试数据形状: {X_test.shape}")

# 保存清洗后的数据 1分
cleaned_file_path = "2.1.3_cleaned_data.csv"
#填充

