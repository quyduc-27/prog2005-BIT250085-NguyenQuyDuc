n = input('nhap so cua ban : ')
tong_cac_cs = 0
for i in n:
    if i.isdigit():
        tong_cac_cs += int(i)
print('tong cac cs cua ban la : ', tong_cac_cs)
