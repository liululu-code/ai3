import pickle

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 加载数据并显示前五行 2分
df = #填充
print #填充

# 处理 horsepower 列和缺失值 2分
df["horsepower"] = #填充
df = #填充

# 定义自变量和因变量 2分
X = #填充
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 初始化包含标准化和线性回归的管道 2分
pipeline = #填充

# 训练线性回归模型 1分
#填充

# 保存线性回归模型 1分
with open("2.2.2_model.pkl", "wb") as model_file:
    #填充

# 使用线性回归模型预测 1分
y_pred = #填充

# 保存线性回归模型预测结果 1分
results_df = pd.DataFrame(y_pred, columns=["预测结果"])
results_filename = "2.2.2_results.txt"
#填充

# 保存线性回归模型测试得分
with open("2.2.2_report.txt", "w") as results_file:
    results_file.write(f"训练集得分: {pipeline.score(X_train, y_train)}\n")
    results_file.write(f"测试集得分: {pipeline.score(X_test, y_test)}\n")

# 初始化随机森林回归模型 1分
rf_model = #填充

# 训练随机森林回归模型 1分
#填充

# 使用随机森林模型预测 1分
y_pred_rf = #填充

# 保存随机森林模型预测结果 1分
results_rf_df = pd.DataFrame(y_pred_rf, columns=["预测结果"])
results_rf_filename = "2.2.2_results_rf.txt"
#填充

# 保存随机森林模型测试得分
with open("2.2.2_report_rf.txt", "w") as results_rf_file:
    results_rf_file.write(f"训练集得分: {rf_model.score(X_train, y_train)}\n")
    results_rf_file.write(f"测试集得分: {rf_model.score(X_test, y_test)}\n")
