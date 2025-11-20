products = {"A": 120, "B": 80, "C": 300, "D": 50}

if "A" in products:
    print("Sản phẩm A có trong từ điển: ", products["A"])
else:
    print("Sản phẩm A đã bị xoá.")
    
sorted_products = dict(sorted(products.items(), key=lambda item: item[1]))
print("Sản phẩm sắp xếp theo giá từ thấp đến cao:", sorted_products)

total_value = sum(products.values())
print(f"Tổng giá trị tất cả sản phẩm: {total_value}")

for key in list(products.keys()):
    if products[key] > 200:
        del products[key]

print("Danh sách sản phẩm sau khi xoá giá > 200:", products)


    