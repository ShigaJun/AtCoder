import math

A, B = map(int, input().split())
if abs(A // B - A / B) < abs(math.ceil(A / B) - A / B):
    print(A // B)
else:
    print(math.ceil(A / B))