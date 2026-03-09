# Chương trình sắp xếp chọn (Selection Sort) theo thứ tự giảm dần
# và in ra mảng sau mỗi bước sắp xếp

# Nhập kích thước mảng
n = int(input("Nhập kích thước mảng: "))

# Nhập các phần tử của mảng
arr = []
print("Nhập các phần tử mảng:")
for i in range(n):
    x = int(input(f"Phần tử thứ {i+1}: "))
    arr.append(x)

# Thuật toán Selection Sort giảm dần
for i in range(n - 1):
    max_index = i
    # Tìm phần tử lớn nhất trong đoạn từ i đến cuối
    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:
            max_index = j

    # Hoán đổi
    arr[i], arr[max_index] = arr[max_index], arr[i]

    # In mảng sau mỗi bước
    print(f"Bước {i+1}: {arr}")

# In kết quả cuối cùng
print("Mảng sau khi sắp xếp giảm dần:", arr)