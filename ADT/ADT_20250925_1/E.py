import math

N = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(N):
    if a[i] != i + 1:
        if a[a[i] - 1] == i + 1:
            ans += 1
    else:
        cnt += 1
ans //= 2
ans += math.comb(cnt, 2)
print(ans)