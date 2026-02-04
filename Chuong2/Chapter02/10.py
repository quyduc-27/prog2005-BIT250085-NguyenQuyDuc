def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)
n = int(input('nhap so cua ban: '))
print('tong day so la: ',tong(n))
