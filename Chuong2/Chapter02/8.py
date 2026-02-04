n = input('nhap so nguyen duong: ')
if int(n) < 1:
    print('nhap lai')
else:
    dao = ''
    for i in n:
        dao = i + dao
    print('so nguoc lai la: ',dao)
