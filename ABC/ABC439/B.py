N = int(input())

appeared = []
while N not in appeared:
    appeared.append(N)
    n = list(str(N))
    for i in range(len(n)):
        n[i] = int(n[i])
    N = 0
    for i in range(len(n)):
        N += n[i] ** 2
    if N == 1:
        print("Yes")
        exit()
print("No")