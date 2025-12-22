# W[i] + P[i] が大きい順にソリから降ろしていく
T = int(input())
for _ in range(T):
    N = int(input())
    W = [0] * N
    P = [0] * N
    l = []
    for i in range(N):
        W[i], P[i] = map(int, input().split())
        l.append([i, W[i] + P[i]])
    l = sorted(l, reverse=True, key=lambda x: x[1])
    sum_w = sum(W)
    sum_p = 0
    i = 0
    ans = N
    while sum_w > sum_p:
        sum_w -= W[l[i][0]]
        sum_p += P[l[i][0]]
        i += 1
        ans -= 1
    print(ans)