N, M = map(int, input().split())
p = [0] * M
f = [0] * M

for i in range(N):
    A, B = map(int, input().split())
    p[A-1] += 1
    f[B-1] += 1
    
for i in range(M):
    print(f[i] - p[i])