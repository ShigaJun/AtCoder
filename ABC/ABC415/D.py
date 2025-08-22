n, m = map(int, input().split())
l = []
for i in range(m):
    a, b = map(int, input().split())
    rate = b / a
    l.append([rate, a, b])
l = sorted(l)
