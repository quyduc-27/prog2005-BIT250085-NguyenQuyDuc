n = int(input('nhap mot so: '))
if n <= 1:
    print (f'{n} khong phai snt')
else:
    for i in range (2,n):
        snt = True
        if n % i == 0:
            snt = False
            break
    if snt:
        print (f'{n} la snt')
    else:
        print (f'{n} khong la snt')