def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

number = int(input("Nhập một số nguyên dương: "))
if number < 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print(f"Số đảo ngược của {number} là:", reverse_number(number))