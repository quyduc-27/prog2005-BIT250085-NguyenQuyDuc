# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Hình 1: tam giác số
print("Hình 1:")
for i in range(1, n + 1):          # từ 1 đến n
    for j in range(1, i + 1):      # in từ 1 đến i
        print(j, end=" ")
    print()                        # xuống dòng

# Hình 2: tam giác sao rỗng
print("Hình 2:")
for i in range(1, n + 1):
    # in khoảng trắng phía trước
    print(" " * (n - i), end="")
    # in các ký tự sao
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:  # cạnh trái, cạnh phải, hoặc dòng cuối
            print("* ", end="")
        else:
            print("  ", end="")         # khoảng trống bên trong
    print()                             # xuống dòng