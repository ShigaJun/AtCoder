T = int(input())
for i in range(T):
    N, H = map(int, input())
    t = [0] * (N + 1)
    h = [H]
    for j in range(N):
        t[i + 1], l, u = map(int, input().split())
        