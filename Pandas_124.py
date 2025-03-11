import pandas as pd

# Dữ liệu nhân viên mẫu
data = {
    'Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Tuấn Kiệt', 'Khánh Hưng', 'Gia Hân', 'Ngọc Tú', 'Trường Minh', 'Linh Mai', 'Thảo Nghi', 'Hương Giang',
             'Minh Tuấn', 'Hải Yến'],
    'Dob': ['12/02/2000', '22/04/2003', '06/08/2002', '02/02/2001', '25/12/1999', '10/03/2001', '20/11/2001',
            '15/07/2000', '13/06/2002', '08/02/2000'],
    'Role': ['Web Developer', 'Tester', 'Business Analyst', 'Mobile App Developer', 'Web Developer', 'Tester',
             'Project Manager', 'Designer', 'Web Developer', 'Tester']
}

# Tạo DataFrame từ dữ liệu nhân viên
df = pd.DataFrame(data)

# 1. Xuất toàn bộ dữ liệu nhân viên ra màn hình console
print("Toàn bộ dữ liệu nhân viên:")
print(df)

# 2. Lọc ra nhân viên sinh năm 2001
df['Dob'] = pd.to_datetime(df['Dob'], format='%d/%m/%Y')  # Đảm bảo định dạng ngày tháng đúng
employees_born_2001 = df[df['Dob'].dt.year == 2001]
print("\nNhân viên sinh năm 2001:")
print(employees_born_2001)

# 3. Xuất TOP 3 nhân viên có tuổi cao nhất
df_sorted_by_age = df.sort_values(by='Dob').head(3)
print("\nTOP 3 nhân viên có tuổi cao nhất:")
print(df_sorted_by_age)

# 4. Lọc ra nhân viên có vai trò là Tester
testers = df[df['Role'] == 'Tester']
print("\nNhân viên có vai trò Tester:")
print(testers)

# 5. Đếm số lượng nhân viên theo vai trò
role_count = df['Role'].value_counts()
print("\nSố lượng nhân viên theo vai trò:")
print(role_count)


# 6. Thêm một hàng mới
def add_new_row():
    symbol = input("Enter Symbol: ")
    price = float(input("Enter Price: "))
    pe = float(input("Enter PE: "))
    usd = float(input("Enter USD: "))

    # Tạo một dictionary cho hàng mới
    new_row = {'Id': len(df) + 1, 'Name': symbol, 'Dob': None,
               'Role': 'Unknown'}  # Thêm một nhân viên mới với thông tin giả
    df.loc[len(df)] = new_row
    print("Dữ liệu nhân viên mới đã được thêm vào.")
    print(df)


# Thêm nhân viên mới
print("\nThêm nhân viên mới:")
add_new_row()


# 7. Xóa nhân viên theo Symbol
def delete_by_symbol(data_frame):
    symbol = input("Enter Symbol to delete: ")

    # Tìm và xóa nhân viên có Symbol khớp
    if symbol in data_frame['Name'].values:
        updated_df = data_frame[data_frame['Name'] != symbol]
        print(f"Nhân viên với tên '{symbol}' đã bị xóa. Dữ liệu cập nhật:")
        print(updated_df)
    else:
        print(f"Không tìm thấy nhân viên có tên '{symbol}'.")
        updated_df = data_frame

    return updated_df


# Xóa nhân viên
print("\nXóa nhân viên theo tên:")
df = delete_by_symbol(df)

# In dữ liệu cuối cùng
print("\nDữ liệu cuối cùng:")
print(df)
