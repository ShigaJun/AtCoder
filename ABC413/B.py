n = int(input())
s = [input() for _ in range(n)]
l = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif s[i] + s[j] not in l:
            l.append(s[i] + s[j])
print(len(l))