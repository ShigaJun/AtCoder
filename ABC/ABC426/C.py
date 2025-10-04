N, Q = map(int, input().split())

OS = [x for x in range(1, N + 1)]
for _ in range(Q):
    X, Y = map(int, input().split())
    OS[Y - 1] += OS[X - 1]