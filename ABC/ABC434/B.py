N, M = map(int, input().split())
C = [[] for _ in range(M)]

for i in range(N):
    A, B = map(int, input().split())
    C[A - 1].append(B)
    
for i in range(len(C)):
    print(sum(C[i]) / len(C[i]))