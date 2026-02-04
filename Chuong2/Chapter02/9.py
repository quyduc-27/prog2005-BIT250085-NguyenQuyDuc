n = input('nhap so nguyen duong: ')
cs_lon_nhat = 0
if int(n) < 10000:
    print('nhap lai')
else:
    for i in n:
        a = int(i)
        if cs_lon_nhat < a:
            cs_lon_nhat = a
    print('chu so lon nhat la: ',cs_lon_nhat)
