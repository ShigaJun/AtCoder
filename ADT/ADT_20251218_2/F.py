N, X = map(int, input().split())
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
dp = [[0] * (X + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(X + 1):
        if dp[i][j] == 1:
            if j + a[i] <= X:
                dp[i + 1][j + a[i]] = 1
            if j + b[i] <= X:
                dp[i + 1][j + b[i]] = 1
if dp[N][X] == 1:
    print("Yes")
else:
    print("No")