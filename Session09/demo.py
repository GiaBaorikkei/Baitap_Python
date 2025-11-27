import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [100,200,300,1000,500,400]

# Khai báo figures và axes
fig, ax = plt.subplots()

# Khai báo dạng lưới
plt.grid()

# Vẽ biểu đồ dựa vào các dữ liệu ở trên
ax.plot(x, y, color='red', linestyle='-', marker='o')

# plt.scatter(x, y, color='blue', marker='x')

# Đặt nhãn tiêu dề cho biểu đồ
ax.set_title('Biểu đồ mẫu')
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')

# Xuất sơ đồ
plt.savefig('demo_plot.png')

# Hiển thị được biểu đồ 
plt.show()  
