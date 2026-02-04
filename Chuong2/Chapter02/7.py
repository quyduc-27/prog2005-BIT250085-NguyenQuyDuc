a = int(input("nhap so thu nhat: "))
b = int(input("nhap so thu hai: "))

if a <= 0 or b <= 0:
    print("nhap lai")

else:
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
print('UCLN cua 2 so la', gcd)