n = int(input("Nhập một số nguyên dương: "))

str_n = str(n)

if str_n == str_n[::-1]:
    print(f"Số {n} là số đối xứng (palindrome).")
else:
    print(f"Số {n} không phải là số đối xứng.")
