N = int(input())

a = [[0] * N for _ in range(N)]

r = 0
c = int((N - 1) / 2)
k = 1
a[r][c] = k
for i in range(N ** 2 - 1):
    if a[(r - 1) % N][(c + 1) % N] == 0:
        r = (r - 1) % N
        c = (c + 1) % N
    else:
        r = (r + 1) % N
    a[r][c] = k + 1
    k += 1

for i in range(N):
    print(*a[i])