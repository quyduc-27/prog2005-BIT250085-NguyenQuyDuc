a = input('nhap chuoi ki tu cua ban : ')
b = input('nhap mot ki tu  : ')
dem = 0
if len(b) > 1 or len(b) < 1:
    print('hay nhap 1 ki tu')
else:
    for i in a:
        if b == i:
            dem += 1

print(f'so lan xuat hien cua {b} la: ',dem)