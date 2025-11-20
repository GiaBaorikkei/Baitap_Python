def is_perfect_number(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

number = int(input("Nhập một số nguyên dương: "))
if is_perfect_number(number):
    print(f"{number} là số hoàn hảo.")
else:
    print(f"{number} không phải là số hoàn hảo.")