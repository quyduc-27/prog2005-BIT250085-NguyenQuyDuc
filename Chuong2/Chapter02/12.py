n = int(input('nhap so n: '))
tong_so_le = 0
for i in range(0,n+1):
    if i % 2 != 0:
        tong_so_le += i
print('tong cac so le trong day so tren la: ',tong_so_le)

