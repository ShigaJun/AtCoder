N = int(input())
A = list(map(int, input().split()))

ans = 0

for l in range(N):
    for r in range(l, N):
        sumA = sum(A[l:r + 1])
        for i in range(l, r + 1):
            if sumA % A[i] == 0:
                break
        else:
            ans += 1
print(ans)