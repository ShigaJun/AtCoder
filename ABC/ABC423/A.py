X, C = map(int, input().split())
ans = 0

i = 0
while True:
    if (1000 + C) * (i + 1) <= X:
        i += 1
    else:
        break

print(1000 * i)