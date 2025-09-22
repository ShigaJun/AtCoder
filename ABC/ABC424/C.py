import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    skill[v] = 1
    for e in l[v]:
        if skill[e] == 0:
            dfs(e)

N = int(input())
l = [[] for _ in range(N + 1)]
skill = [1] + [0] * N
for i in range(1, N + 1):
    A, B = map(int, input().split())
    l[A].append(i)
    l[B].append(i)

dfs(0)
print(sum(skill) - 1)