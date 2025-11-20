import math
def circle_area(radius):
    return math.pi * radius * radius

interval_radius = float(input("Nhập bán kính hình tròn: "))
print(f"Diện tích hình tròn có bán kính {interval_radius} là:", circle_area(interval_radius))