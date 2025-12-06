W, B = map(int, input().split())
n = 1
while W * 1000 >= n * B:
    n += 1
print(n)