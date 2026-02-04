a = int(input('chon bang cuu chuong cua '))
if a < 1 or a > 9:
    print('vui long nhap lai cac so trong khoang tu 1 den 9')
else:
    for i in range(1,10):
        print(f'{a}*{i}={a*i}')