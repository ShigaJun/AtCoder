while True:
    N, M, P = map(int, input().split())
    if N == M == P ==0:
        break
    X = [int(input()) for _ in range(N)]
    if X[M - 1] == 0:
        print(0)
    else:
        print(sum(X) * (100 - P) // X[M - 1])
