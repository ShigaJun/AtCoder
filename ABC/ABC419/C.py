import math

n = int(input())
r = [0] * n
c = [0] * n
for i in range(n):
    r[i], c[i] = map(int, input().split())
center_x = math.ceil((min(r) + max(r)) / 2)
center_y = math.ceil((min(c) + max(c)) / 2)
ans = 0
for i in range(n):
    chebyshev = max(abs(center_x - r[i]), abs(center_y - c[i]))
    ans = max(chebyshev, ans)
print(ans)
