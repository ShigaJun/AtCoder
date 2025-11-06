N = int(input())
R = [0] * N
C = [0] * N
for i in range(N):
    R[i], C[i] = map(int, input().split())

center_x = (min(R) + max(R)) // 2
center_y = (min(C) + max(C)) // 2

dis = []

for i in range(N):
    dis.append(max(abs(center_x - R[i]), abs(center_y - C[i])))
print(max(dis))