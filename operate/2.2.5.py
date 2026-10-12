import pickle

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# 加载数据集并显示前五行 2分
df = #填充
print #填充

# 选择特征并将分类变量转换为数值变量 1分
X = #填充
X = #填充

# 设置目标变量 1分
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 初始化决策树回归模型 2分
dt_model = #填充

# 训练决策树回归模型 2分
#填充

# 保存模型 1分
with open("2.2.5_model.pkl", "wb") as model_file:
    #填充

# 在测试集上预测 1分
y_pred = #填充

# 保存预测结果 1分
results = pd.DataFrame({"实际值": y_test, "预测值": y_pred})
results_filename = "2.2.5_results.txt"
#填充

# 生成模型测试报告 2分，其中三个指标各1分
report_filename = "2.2.5_report.txt"
with open(report_filename, "w") as file:
    file.write(f"均方误差: {#填充}\n")
    file.write(f"平均绝对误差: {#填充}\n")
    file.write(f"决定系数: {#填充}\n")
