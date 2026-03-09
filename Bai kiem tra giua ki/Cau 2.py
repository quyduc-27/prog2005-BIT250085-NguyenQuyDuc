import math

# 1. In ra các số lẻ từ 17 đến 111 (giảm dần)
print("Các số lẻ từ 17 đến 111 (giảm dần):")
for i in range(111, 16, -1):   # duyệt từ 111 xuống 17
    if i % 2 != 0:             # kiểm tra số lẻ
        print(i, end=" ")
print("\n")  # xuống dòng

# 2. Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

# In ra các số nguyên tố từ 17 đến 111
print("Các số nguyên tố từ 17 đến 111:")
for i in range(17, 112):       # duyệt từ 17 đến 111
    if is_prime(i):
        print(i, end=" ")