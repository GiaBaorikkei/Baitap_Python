import seaborn as sns
import matplotlib.pyplot as plt

# Tải dữ liệu mẫu từ seaborn
data = sns.load_dataset("tips")

# Thiết lập khung biểu đồ
plt.figure(figsize=(10, 6))

# histplot (histogarm)
# phân tích chiều dài của chim cánh cụt
# sns.histplot(data=data, x="total_bill", bins=60, color='skyblue', kde=True)
# plt.show()

#kdeplot
sns.kdeplot(data=data, x="total_bill", fill=True, linewidth=2)
plt.show()