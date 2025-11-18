a = int(input("Nhập một số nguyên: "))

if a % 3 == 0 and a % 5 == 0:
    print(f"Số {a} chia hết cho cả 3 và 5")
elif a % 3 == 0:
    print(f"Số {a} chia hết cho 3")
elif a % 5 == 0:
    print(f"Số {a} chia hết cho 5")
else:
    print(f"Số {a} không chia hết cho 3 hoặc 5")
