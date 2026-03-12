import math
data = "5; 7; 8; -2; 8; 11; 13; 9; 10"
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
numbers = [int(x.strip()) for x in data.split(";")]
print("tung so tren 1 dong:")
for n in numbers: print(n)
chan = len([x for x in numbers if x % 2 == 0])
am = len([x for x in numbers if x < 0])
nguyen_to = len([x for x in numbers if is_prime(x)])
trung_binh = sum(numbers) / len(numbers)
print(f"so chan: {chan}")
print(f"so am: {am}")
print(f"so nguyen to: {nguyen_to}")
print(f"trung binh: {trung_binh}")