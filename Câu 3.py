n = int(input("nhap so mot bat ki tu 1 den 9: "))

if 1 <= n <= 9:
    print(f"bang cuu chuong {n}")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")
else:
    print("loi")