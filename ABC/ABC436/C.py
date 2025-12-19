N, M = map(int, input().split())
R = [0] * M
C = [0] * M
S = []
cnt = 0
for i in range(M):
    R[i], C[i] = map(int, input().split())
    S.append(R - 1, C - 1)
    S.append(R, C - 1)
    S.append(R - 1, C)
    S.append(R, C)

print(cnt)