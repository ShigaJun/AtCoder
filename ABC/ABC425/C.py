N, Q = map(int, input().split())
A = list(map(int, input().split()))
newA = [0] * (N + 1)

for i in range(1, N + 1):
    newA[i] = newA[i - 1] + A[i - 1]

start = 0
lIdx = rIdx = 0
ans = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        start += query[1]
    else:
        lIdx = (start + query[1]) % N
        if lIdx == 0:
            lIdx = N
        rIdx = (start + query[2]) % N
        if rIdx == 0:
            rIdx = N
        if lIdx > rIdx:
            ans = (newA[N] - newA[lIdx - 1]) + (newA[rIdx] - newA[0])
        else:
            ans = newA[rIdx] - newA[lIdx - 1]
        print(ans)