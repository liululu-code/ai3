import pickle

import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 加载数据并显示前五行 2分
data = #填充
print #填充

# 选择自变量和因变量
X = #填充
y = #填充

# 划分训练集和测试集 1分
X_train, X_test, y_train, y_test = #填充

# 初始化 Logistic 回归模型 2分
model = #填充

# 训练 Logistic 回归模型 2分
#填充

# 保存模型 1分
with open("2.2.1_model.pkl", "wb") as file:
    #填充

# 在测试集上预测 1分
y_pred = #填充
pd.DataFrame(y_pred, columns=["预测结果"]).to_csv("2.2.1_results.txt", index=False)

# 生成测试报告
report = #填充
with open("2.2.1_report.txt", "w") as file:
    file.write(report)

# 计算并显示准确率 2分
accuracy = #填充
print(f"模型准确率: {accuracy:.2f}")

# 使用 SMOTE 处理数据不平衡 2分
smote = #填充
X_resampled, y_resampled = #填充

# 使用重新采样的数据训练模型 2分
#填充

# 生成新的预测结果 1分
y_pred_resampled = #填充
pd.DataFrame(y_pred_resampled, columns=["预测结果"]).to_csv(
    "2.2.1_results_xg.txt", index=False
)

# 生成新的测试报告
report_resampled = #填充
with open("2.2.1_report_xg.txt", "w") as file:
    file.write(report_resampled)

# 分析新的测试结果 1分
accuracy_resampled = #填充
print(f"重新采样后的模型准确率: {accuracy_resampled:.2f}")

