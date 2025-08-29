N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for i in range(N):
    ans += min(A[i], B[i])
for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X), int(V)
    ans -= min(A[X - 1], B[X - 1]) # 一度，対象インデックスの min を引いておく
    if c == 'A':
        A[X - 1] = V
    else:
        B[X - 1] = V
    ans += min(A[X - 1], B[X - 1]) # 更新後の対象インデックスの min を足す
    print(ans)