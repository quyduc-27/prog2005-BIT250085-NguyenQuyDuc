a = int(input('nhap so duong :'))
if a < 2 :
    print(f'{a} khong phai snt')
else:
    SNT=True
    for i in range(2,a):
        if a % i == 0:
            SNT=False
            break
    if SNT:
        print(f'{a} la snt')
    else:
        print(f'{a} khong phai snt')

