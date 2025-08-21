import math
import numpy as np

n = int(input())
r, c = [0] * n
for i in range(n):
    r[i], c[i] = map(int, int(input()))
center_x = math.ceil((min(r) + max(r)) / 2)
center_y = math.ceil((min(c) + max(c)) / 2)
for i in range(n):
