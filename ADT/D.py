h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
l = ('s', 'n', 'u', 'k', 'e')
d = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
for i in range(h):
    for j in range(w):
        if s[i][j] == 's':
            for k in d:
                ans = [[i + 1, j + 1]]
                c = [i, j]
                for m in range(1, 5):
                    c = [c[0] + k[0], c[1] + k[1]]
                    if 0 <= c[0] < h and 0 <= c[1] < w:
                        if s[c[0]][c[1]] == l[m]:
                            ans.append([c[0] + 1, c[1] + 1])
                        else:
                            break
                    else:
                        break
                else:
                    for a in ans:
                        print(*a)