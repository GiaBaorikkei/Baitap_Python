def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total  
number = int(input("Nhập một số nguyên dương: "))
if number < 0:
    print("Vui lòng nhập số nguyên dương.") 
else:
    print(f"Tổng các chữ số trong {number} là:", sum_of_digits(number)) 