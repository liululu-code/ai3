import pandas as pd

# 加载数据集并显示数据集的前五行 1分
data = pd.read_csv('doc/1.1.1答案/patient_data.csv')#填充
print("数据集的前五行:")
print(data.head()) #填充

# 显示每一列的数据类型
print(data.dtypes)

# 检查缺失值并删除缺失值所在的行  2分
print("\n检查缺失值:")
print(data.isnull()) #填充
data = data.drop_duplicates(inplace=True) #填充

# 将 'horsepower' 列转换为数值类型，并处理转换中的异常值 1分
data['horsepower'] = (data['horsepower'], errors='coerce')#填充(data['horsepower'], errors='coerce')
data = #填充

# 显示每一列的数据类型
print(data.horsepower.dtypes)

# 检查清洗后的缺失值
print("\n检查清洗后的缺失值:")
print(data.isnull().sum())

from sklearn.preprocessing import StandardScaler

# 对数值型数据进行标准化处理 1分
numerical_features = #填充
scaler = #填充
data[numerical_features] = #填充

from sklearn.model_selection import train_test_split

# 选择特征和目标变量 2分
selected_features = #填充
X = #填充
y = #填充

# 划分数据集为训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 将特征和目标变量合并到一个数据框中
cleaned_data = X.copy()
cleaned_data['mpg'] = y

# 保存清洗和处理后的数据 1分
#填充

# 打印消息指示文件已保存
print("\n清洗后的数据已保存到 2.1.1_cleaned_data.csv")

