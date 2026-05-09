N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))

B = [[] for _ in range(N)]
for i in range(N):
    B[i] = [A[i], C[i]]
i = 0
cnt = 0
while cnt + B[i][0][0] * B[i][1] < K:
    cnt += B[i][0][0] * B[i][1]
    i += 1
if (K - cnt) % B[i][0][0] == 0:
    j = B[i][0][0]
else:
    j = (K - cnt) % B[i][0][0]
print(B[i][0][j])