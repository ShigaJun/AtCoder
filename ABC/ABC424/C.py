N = int(input())
l = [[0] * N] * N
skill = []
ans = []
for i in range(N):
    A, B = map(int, input().split())
    if A == B == 0:
        skill.append(i + 1)
        continue
    l[A][i] = 1
    l[B][i] = 1

for s in skill:
    