import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取信用数据集
data = #填充

# 统计数据缺失值和重复值 各2分
missing_values = #填充
duplicate_values = #填充
print("缺失值统计:")
print(missing_values)
print("重复值统计:")
print(duplicate_values)

# 审核年龄、收入、贷款金额和信用评分的合理性 各2分
data["is_age_valid"] = #填充
data["is_income_valid"] = #填充
data["is_loan_amount_valid"] = #填充
data["is_credit_score_valid"] = #填充

# 汇总每行数据的合理性检查结果
validity_checks = #填充
data["is_valid"] = validity_checks
print("数据合理性检查:")
print(
    data[
        [
            "is_age_valid",
            "is_income_valid",
            "is_loan_amount_valid",
            "is_credit_score_valid",
            "is_valid",
        ]
    ].describe()
)

# 找出并删除不合理数据
invalid_rows = #填充
cleaned_data = #填充

# 删除审核标记列
audit_columns = [
    "is_age_valid",
    "is_income_valid",
    "is_loan_amount_valid",
    "is_credit_score_valid",
    "is_valid",
]
cleaned_data = #填充

# 保存清洗后的数据 2分
cleaned_file_path = "cleaned_credit_data.csv"
#填充
print("数据清洗完成，已保存为 'cleaned_credit_data.csv'")

