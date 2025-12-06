import sys
 
sys.setrecursionlimit(10 ** 5)

def solve(G, p, t):
    if G[p][t] == 1:
        return True
    elif sum(G[p]) == 0:
        return False
    else:
        for i in range(M):
            if i != p:
                if solve(G, i, t):
                    return True
        else:
            return False
        
N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for i in range(M):
    X, Y = map(int, input().split())
    G[X - 1][Y - 1] = 1
for i in range(N):
    for j in range(N):
        if i != j:
            if solve(G, i, j):
                G[i][j] = 1
Q = int(input())
isBlack = [0] * N
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        isBlack[query[1] - 1] = 1
    else:
        for i in range(N):
            if isBlack[i] == 1 and i != query[1] - 1:
                if solve(G, query[1] - 1, i):
                    print("Yes")
        else:
            print("No")