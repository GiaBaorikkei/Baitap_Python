import json
students = []
# Hiển thị sanh sách sinh viên từ file JSON
def display_students():
    global students
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            students = data.get("students", [])
            print(f"{'Mã SV':<10}{'Họ Tên':<20}{'Toán':<10}{'Lý':<10}{'Hóa':<10}{'Điểm TB':<10}{'Xếp Loại':<10}")
            for student in students:
                print(f"{student['id']:<10}{student['ten']:<20}{student['diem_toan']:<10}{student['diem_ly']:<10}{student['diem_hoa']:<10}{student['diem_tb']:<10}{student['xep_loai']:<10}")
    except FileNotFoundError:
        print("Chưa có dữ liệu sinh viên.")

# Thêm sinh viên mới
def add_student():
    global students
    id = input("Nhập mã sinh viên: ")
    ten = input("Nhập họ tên sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    diem_tb = (diem_toan + diem_ly + diem_hoa) / 3

    if diem_tb >= 8:
        xep_loai = "Giỏi"
    elif diem_tb >= 6.5:
        xep_loai = "Khá"
    elif diem_tb >= 5:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    new_student = {
        "id": id,
        "ten": ten,
        "diem_toan": diem_toan,
        "diem_ly": diem_ly,
        "diem_hoa": diem_hoa,
        "diem_tb": round(diem_tb, 2),
        "xep_loai": xep_loai
    }

    students.append(new_student)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump({"students": students}, file, ensure_ascii=False, indent=4)

    print("Đã thêm sinh viên mới thành công!")
    
# Cập nhật thông tin sinh viên
def update_student():
    id = input("Nhập mã sinh viên cần cập nhật: ")
    for student in students:
        if student['id'] == id:
            print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
            ten = input(f"Họ tên ({student['ten']}): ") or student['ten']
            diem_toan = input(f"Điểm Toán ({student['diem_toan']}): ")
            diem_ly = input(f"Điểm Lý ({student['diem_ly']}): ")
            diem_hoa = input(f"Điểm Hóa ({student['diem_hoa']}): ")

            student['ten'] = ten
            if diem_toan:
                student['diem_toan'] = float(diem_toan)
            if diem_ly:
                student['diem_ly'] = float(diem_ly)
            if diem_hoa:
                student['diem_hoa'] = float(diem_hoa)

            diem_tb = (student['diem_toan'] + student['diem_ly'] + student['diem_hoa']) / 3
            student['diem_tb'] = round(diem_tb, 2)

            if diem_tb >= 8:
                student['xep_loai'] = "Giỏi"
            elif diem_tb >= 6.5:
                student['xep_loai'] = "Khá"
            elif diem_tb >= 5:
                student['xep_loai'] = "Trung bình"
            else:
                student['xep_loai'] = "Yếu"

            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump({"students": students}, file, ensure_ascii=False, indent=4)

            print("Đã cập nhật thông tin sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên với mã đã nhập.")
    
# Xóa sinh viên
def delete_student():
    id = input("Nhập mã sinh viên cần xóa: ")
    for i, student in enumerate(students):
        if student['id'] == id:
            del students[i]
            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump({"students": students}, file, ensure_ascii=False, indent=4)
            print("Đã xóa sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên với mã đã nhập.")

# Lưu lại vào file JSON trước khi thoát
def save_and_exit():
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump({"students": students}, file, ensure_ascii=False, indent=4)
    print("Đã lưu dữ liệu và thoát chương trình.")
    
# Menu chức năng
def menu():
    while True:
        print("\nQuản Lý Sinh Viên")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp sinh viên")
        print("7. Thống kê điểm trung bình")
        print("8. Vẽ biểu đồ thống kê")
        print("9. Lưu vào file JSON")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-9): ")
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '0':
            save_and_exit()
            break
        else:
            print("Chức năng chưa được triển khai hoặc không hợp lệ.")
            
menu()

