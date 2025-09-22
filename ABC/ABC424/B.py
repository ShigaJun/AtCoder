N, M, K = map(int, input().split())

cnt = [0] * N
ans = []
for i in range(K):
    A, B = map(int, input().split())
    cnt[A - 1] += 1
    if cnt[A - 1] == M:
        ans.append(A)
print(*ans)