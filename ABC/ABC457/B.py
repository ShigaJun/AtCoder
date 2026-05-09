N = int(input())
L = [0] * N
A = [[] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
    L[i] = A[i].pop(0)
X, Y = map(int, input().split())

print(A[X - 1][Y - 1])