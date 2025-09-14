N, R = map(int, input().split())
L = list(map(int, input().split()))
x = 0

i = 0
while R > i and L[i] == 1:
    x += 1
    i += 1
i = 0
while R < N - 1 - i and L[N - 1 - i] == 1:
    x += 1
    i += 1

ans = (sum(L) - x) + (len(L) - x)
print(ans)