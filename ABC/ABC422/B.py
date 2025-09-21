import math

H, W = map(int, input().split())
S = [input() for _ in range(H)]
dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

def func(i, j):
    cnt = 0
    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]
        if 0 <= di < H and 0 <= dj < W:
           if S[int(di)][int(dj)] == '#':
               cnt += 1
    if cnt == 2 or cnt == 4:
        return True
    else:
        return False

for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and not(func(i, j)):
            print("No")
            exit()
print("Yes")