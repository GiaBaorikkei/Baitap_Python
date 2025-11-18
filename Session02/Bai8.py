a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))

if a + b > c and a + c > b and b + c > a:
    print("Là 3 cạnh tam giác")
else:
    print("Không phải 3 cạnh tam giác")
