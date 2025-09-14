N, R = map(int, input().split())
L = list(map(int, input().split()))

if L.count(0) == 0:
    print(0)
    exit()

for i, v in enumerate(L):
    if v == 0:
        l = min(i, R)
        break
for j, v in enumerate(reversed(L)):
    if v == 0:
        r = max(N - 1 - j, R - 1)
        break

ans = sum(L[l:r + 1]) + (r - l + 1)
print(ans)