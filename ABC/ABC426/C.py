N, Q = map(int, input().split())

OS = [1] * N
oldest = 1
for _ in range(Q):
    X, Y = map(int, input().split())
    sum_old = 0
    for i in range(oldest, X + 1):
        sum_old += OS[oldest - 1]
        OS[oldest - 1] = 0
        oldest += 1
    print(sum_old)
    OS[Y - 1] += sum_old