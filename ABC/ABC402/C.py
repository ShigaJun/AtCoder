from collections import Counter

N, M = map(int, input().split())
K = [0] * M
A = []
C = [[] for _ in range(N)] # ある食材が含まれる料理
for i in range(M):
    A.append(list(map(int, input().split())))
    K[i] = A[i].pop(0)
    for j in range(K[i]):
        C[A[i][j] - 1].append(i)
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    for c in (C[B[i] - 1]):
        K[c] -= 1
        if K[c] == 0:
            ans += 1
    print(ans)