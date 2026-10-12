from datetime import datetime

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 加载数据集并指定编码为 gbk 1分
data = #填充

# 查看数据类型、表结构和缺失值 1分
print(data.dtypes)
print #填充
print(data.isnull().sum())

# 规范日期格式
data["就诊日期"] = #填充
data["诊断日期"] = #填充

# 修改列名 1分
#填充
print(data.head())

# 增加诊断延迟和病程列 1分
data["诊断延迟"] = #填充
data["病程"] = #填充

# 删除不合理的数据 1分
data = #填充
print(data.describe())

# 删除重复值并记录删除的行数 1分
initial_rows = data.shape[0]
#填充
deleted_rows = initial_rows - data.shape[0]
print(f"删除的重复行数: {deleted_rows}")

# 对指定列进行归一化处理 1分
scaler = #填充
columns_to_normalize = #填充
data[columns_to_normalize] = #填充
print(data.head())

# 统计不同疾病类型的治疗结果分布
treatment_outcome_distribution = #填充

# 设置中文字体
font_path = "C:/Windows/Fonts/simhei.ttf"
my_font = fm.FontProperties(fname=font_path)

# 绘制治疗结果柱状图 1分
#填充
plt.title("不同疾病类型的治疗结果分布", fontproperties=my_font)
plt.xlabel("疾病类型", fontproperties=my_font)
plt.ylabel("治疗结果数量", fontproperties=my_font)
plt.xticks(fontproperties=my_font)
plt.yticks(fontproperties=my_font)
plt.legend(prop=my_font)
plt.show()

# 绘制年龄和疾病严重程度散点图 1分
#填充
plt.title("年龄和疾病严重程度的关系", fontproperties=my_font)
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("疾病严重程度", fontproperties=my_font)
plt.xticks(fontproperties=my_font)
plt.yticks(fontproperties=my_font)
plt.show()

# 保存处理后的数据 1分
output_path = "2.1.4_cleaned_data.csv"
#填充

