X, Y = map(int, input().split())
a = [X, Y]

for i in range(2, 10):
    x = str(a[i - 1] + a[i - 2])
    rev_x = "".join(reversed(x))
    a.append(int(rev_x))
print(a[9])