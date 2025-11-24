import math

x, y, z = map(int, input().split())
a = (x - y * z) / (z - 1)

if a - math.floor(a) != 0:
    print("No")
    exit()

if a >= 0:
    print("Yes")
else:
    print("No")