N = int(input())
A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(N):
    A[i] = list(input())
for i in range(N):
    B[i] = list(input())

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
            exit()