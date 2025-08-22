n, k, x = map(int, input().split())
s = [input() for _ in range(n)]
l = []

def dfs(crr, count):
    if count == k:
        l.append(crr)
        return
    for s_a in s:
        dfs(crr + s_a, count + 1)

dfs("", 0)
l.sort()
print(l[x - 1])