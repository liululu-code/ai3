import pickle

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# 加载数据集并显示前五行 2分
df = #填充
print #填充

# 清理字符串字段和列名
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.columns = df.columns.str.strip()

# 选择特征并将分类变量转换为数值变量 1分
X = #填充
X = #填充

# 将年龄段转换为数值目标变量 1分
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 初始化随机森林回归模型 1分
rf_model = #填充

# 训练随机森林回归模型 1分
#填充

# 保存随机森林模型 1分
with open("2.2.3_model.pkl", "wb") as model_file:
    #填充

# 使用随机森林模型预测 1分
y_pred = #填充
results_df = pd.DataFrame(y_pred, columns=["预测结果"])
results_df.to_csv("2.2.3_results.txt", index=False)

# 计算训练集和测试集分数 1分
train_score = #填充
test_score = #填充

# 计算均方误差和决定系数 各1分
mse = #填充
r2 = #填充
with open("2.2.3_report.txt", "w") as report_file:
    report_file.write(f"训练集得分: {train_score:.4f}\n")
    report_file.write(f"测试集得分: {test_score:.4f}\n")
    report_file.write(f"均方误差(MSE): {mse:.4f}\n")
    report_file.write(f"决定系数(R^2): {r2:.4f}\n")

# 初始化并训练 XGBoost 回归模型 各1分
xgb_model = #填充
#填充

# 使用 XGBoost 模型预测 1分
y_pred_xgb = #填充
results_df_xgb = pd.DataFrame(y_pred_xgb, columns=["预测结果"])
results_df_xgb.to_csv("2.2.3_results_xgb.txt", index=False)

# 计算并保存 XGBoost 评估指标
with open("2.2.3_report_xgb.txt", "w") as xgb_report_file:
    xgb_report_file.write(f"XGBoost训练集得分: {#填充}\n")
    xgb_report_file.write(f"XGBoost测试集得分: {#填充}\n")
    xgb_report_file.write(f"XGBoost均方误差(MSE): {#填充}\n")
    xgb_report_file.write(f"XGBoost决定系数(R^2): {#填充}\n")

