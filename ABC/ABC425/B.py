N = int(input())
A = list(map(int, input().split()))
P = [-1] * N

for i in range(N):
    if A[i] != -1:
        if A[i] in P:
            print("No")
            exit()
        else:
            P[i] = A[i]

for i in range(1, N + 1):
    if i not in P:
        P[P.index(-1)] = i
print("Yes")
print(*P)