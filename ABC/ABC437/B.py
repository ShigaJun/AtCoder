H, W, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [int(input()) for _ in range(N)]

cnt = [0] * N
for i in range(H):
    for j in range(W):
        for k in range(N):
            if A[i][j] == B[k]:
                cnt[i] += 1
print(max(cnt))