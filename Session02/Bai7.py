a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ 2: "))

tong = 0

for i in range(a + 1, b):
    tong += i

print(f"Tổng từ {a} đến {b} là: {tong}")
