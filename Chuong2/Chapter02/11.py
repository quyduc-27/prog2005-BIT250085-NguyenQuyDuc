a = float(input('nhap diem tb cua ban: '))
if a >= 8:
    print('xep loai gioi')
elif a >= 6.5 and a <= 7.9:
    print('xep loai kha')
elif a >= 5.0 and a <= 6.4:
    print('xep loai trung binh')
else:
    print ('xep loai yeu')