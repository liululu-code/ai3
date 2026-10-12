import numpy as np
import pandas as pd

# 读取患者数据集 1分
data = #填充

# 根据住院天数创建风险等级列 3分
data["RiskLevel"] = #填充

# 统计不同风险等级的患者数量 2分
risk_counts = #填充

# 计算高风险和低风险患者占比 各1分
high_risk_ratio = #填充
low_risk_ratio = #填充

print("高风险患者数量:", risk_counts["高风险患者"])
print("低风险患者数量:", risk_counts["低风险患者"])
print("高风险患者占比:", high_risk_ratio)
print("低风险患者占比:", low_risk_ratio)

# 定义 BMI 区间和标签
bmi_bins = [0, 18.5, 24, 28, np.inf]
bmi_labels = ["偏瘦", "正常", "超重", "肥胖"]

# 根据 BMI 值划分区间 4分
data["BMIRange"] = #填充

# 计算每个 BMI 区间中高风险患者的比例 2分
bmi_risk_rate = #填充

# 统计每个 BMI 区间的患者数量 1分
bmi_patient_count = #填充

print("BMI区间中高风险患者的比例和患者数:")
print(bmi_risk_rate)
print(bmi_patient_count)

# 定义年龄区间和标签
age_bins = [0, 26, 36, 46, 56, 66, np.inf]
age_labels = ["≤25岁", "26-35岁", "36-45岁", "46-55岁", "56-65岁", "＞65岁"]

# 根据年龄值划分区间 4分
data["AgeRange"] = #填充

# 计算每个年龄区间中高风险患者的比例 2分
age_risk_rate = #填充

# 统计每个年龄区间的患者数量 1分
age_patient_count = #填充

print("年龄区间中高风险患者的比例和患者数:")
print(age_risk_rate)
print(age_patient_count)

