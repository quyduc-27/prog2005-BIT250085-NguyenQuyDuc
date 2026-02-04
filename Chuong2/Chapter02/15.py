n = input('nhap so nguyen duong :')
tong_cac_cs = 0
i=0
if int(n) < 1:
    print('nhap lai')
else:
    while i<len(n):
        tong_cac_cs += int(n[i])
        i += 1
    print('tong cac chu so la: ',tong_cac_cs)

