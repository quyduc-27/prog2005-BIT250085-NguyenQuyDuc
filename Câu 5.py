import random
M = int(input("nhap M: "))
N = int(input("nhap N: "))
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
for row in matrix:
    print(row)
r = int(input(f"nhap hang muon xem : "))
print(f"hang {r}: {matrix[r]}")
c = int(input(f"nhap cot muon xem: "))
col_data = [matrix[i][c] for i in range(M)]
print(f"cot {c}: {col_data}")
max_val = max(max(row) for row in matrix)
print(f"gia tri lon nhat: {max_val}")
