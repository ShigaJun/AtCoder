N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
min_list = []

for i in range(N):
    min_list.append(min(A[i], B[i]))
ans = sum(min_list)
for i in range(Q):
    c, X, V = input().split()
    X, V = int(X), int(V)
    if c == 'A':
        A[X - 1] = V
    else:
        B[X - 1] = V
    diff = min(A[X - 1], B[X - 1]) - min_list[X - 1]
    min_list[X - 1] = min(A[X - 1], B[X - 1])
    ans += diff
    print(ans)