import itertools

N = int(input())

l1 = list(itertools.permutations(range(1, 3163), 2))
l2 = []
for i in range(len(l1)):
    x = l1[i][0]
    y = l1[i][1]
    if x >= y:
        continue
    e = x ** 2 + y ** 2
    if e <= N:
        if e not in l2:
            l2.append(e)
        else:
            l2.remove(e)
print(len(l2))
print(*sorted(l2))