import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# 加载数据集并显示前五行 2分
data = #填充
print #填充

# 删除不必要的列 1分，并将分类变量转换为哑变量
data_cleaned = #填充
data_cleaned = #填充

# 定义目标字段
target = "5.您进行过绿色低碳的相关生活方式吗?"

# 定义自变量和因变量 2分
X = #填充
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 初始化并训练线性回归模型 各1分
model = #填充
#填充

# 保存线性回归模型 1分
model_filename = "2.2.4_model.pkl"
#填充

# 使用线性回归模型预测 1分
y_pred = #填充

# 保存线性回归模型预测结果 1分
results = pd.DataFrame({"实际值": y_test, "预测值": y_pred})
results_filename = "2.2.4_results.txt"
#填充

# 计算并保存均方误差和决定系数 2分
report_filename = "2.2.4_report.txt"
with open(report_filename, "w") as file:
    file.write(f"均方误差: {#填充}\n")
    file.write(f"决定系数: {#填充}\n")

# 初始化并训练 XGBoost 模型 各1分
xgb_model = #填充
#填充

# 使用 XGBoost 模型预测 1分
y_pred_xg = #填充

# 保存 XGBoost 预测结果
results_xg_filename = "2.2.4_results_xg.txt"
results_xg = pd.DataFrame({"实际值": y_test, "预测值": y_pred_xg})
results_xg.to_csv(results_xg_filename, index=False, sep="\t")

# 计算并保存 XGBoost 评估指标 1分
report_filename_xgb = "2.2.4_report_xgb.txt"
with open(report_filename_xgb, "w") as file:
    file.write(f"均方误差: {#填充}\n")
    file.write(f"决定系数: {#填充}\n")

