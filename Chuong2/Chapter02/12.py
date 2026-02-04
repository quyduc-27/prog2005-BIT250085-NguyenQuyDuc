n = int(input('nhap n: '))
tong_so_le = 0
for i in range(0,n+1):
    if i % 2 != 0:
        tong_sl += i
print('tong cac so le trong day so tren la: ',tong_sl)
