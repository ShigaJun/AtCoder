H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = list(input())
X -= 1
Y -= 1
if S[X][Y] != '@':
    C = 0
else:
    C = 1
for i in range(len(T)):
    flag = 0
    if T[i] == 'U' and S[X - 1][Y] != '#':
        X -= 1
        flag = 1
    elif T[i] == 'D' and S[X + 1][Y] != '#':
        X += 1
        flag = 1
    elif T[i] == 'L' and S[X][Y - 1] != '#':
        Y -= 1
        flag = 1
    elif T[i] == 'R' and S[X][Y + 1] != '#':
        Y += 1
        flag = 1
    if flag == 1 and S[X][Y] == '@':
        C += 1
        S[X][Y] = '.'
print(X + 1, Y + 1, C)