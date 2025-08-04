r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
l = [0]
for i in range(r):
    for j in range(c):
        if b[i][j] != '.' and b[i][j] != '#':
            power = int(b[i][j])
            b[i][j] = '.'
            for k in range(r):
                for l in range(c):
                    if abs(i - k) + abs(j - l) <= power and b[k][l] == '#':
                        b[k][l] = '.'
for i in range(r):
    # for j in range(c):
    #     if b[i][j] != '.' and b[i][j] != '#':
    #         b[i][j] = '.'
    print(''.join(b[i]))