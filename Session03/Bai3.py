def factorial(n):   
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Nhập một số nguyên không âm: "))
if number < 0:
    print("Vui lòng nhập số không âm.")
else:
    print(f"Giai thừa của {number} là: {factorial(number)}")