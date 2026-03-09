import math

# ---------------- Bài 1 ----------------
def bai1():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    # Tìm max, min
    print("Số lớn nhất:", max(a, b, c))
    print("Số nhỏ nhất:", min(a, b, c))

    # Giải phương trình bậc hai
    if a == 0:
        if b == 0:
            print("Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm")
        else:
            print("Nghiệm:", -c/b)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            print("Nghiệm kép:", -b/(2*a))
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Hai nghiệm:", x1, x2)

# ---------------- Bài 2 ----------------
def bai2():
    print("Các số lẻ từ 17 đến 111 (giảm dần):")
    for i in range(111, 16, -1):
        if i % 2 == 1:
            print(i, end=" ")
    print("\n")

    print("Các số nguyên tố từ 17 đến 111:")
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                return False
        return True

    for i in range(17, 112):
        if is_prime(i):
            print(i, end=" ")
    print()

# ---------------- Bài 3 ----------------
def bai3():
    n = int(input("Nhập n: "))

    print("Hình 1:")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    print("Hình 2:")
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(i+1):
            if j == 0 or j == i or i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# ---------------- Bài 4 ----------------
def bai4():
    size = int(input("Nhập kích thước mảng: "))
    arr = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(size)]

    for i in range(size-1):
        max_idx = i
        for j in range(i+1, size):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        print("Bước", i+1, ":", arr)

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Bài 1")
        print("2. Bài 2")
        print("3. Bài 3")
        print("4. Bài 4")
        print("5. Thoát")

        choice = input("Chọn chương trình: ")

        if choice == "1":
            bai1()
        elif choice == "2":
            bai2()
        elif choice == "3":
            bai3()
        elif choice == "4":
            bai4()
        elif choice == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    menu()