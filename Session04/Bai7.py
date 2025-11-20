products = {"A": 120, "B": 80, "C": 300, "D": 50}

products = {k: v for k, v in products.items() if v < 100}
print("Sản phẩm có giá < 100:", products)
print(f"Danh sách các sản phẩm còn lại: {list(products.keys())}")

products["E"] = 90
print("Cập nhật danh sách sản phẩm:", products)

print(f"Số lượng sản phẩm còn lại: {len(products)}")
