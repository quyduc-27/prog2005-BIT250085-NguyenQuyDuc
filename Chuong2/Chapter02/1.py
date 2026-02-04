a = int(input('chon bang cuu chuong '))
if a < 1 or a > 9:
    print('vui long nhap lai ')
else:
    for i in range(1,10):

        print(f'{a}*{i}={a*i}')
