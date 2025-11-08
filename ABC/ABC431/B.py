X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

judge = [0] * N

for _ in range(Q):
    P = int(input())
    if judge[P - 1] == 0:
        judge[P - 1] = 1
    else:
        judge[P - 1] = 0
    
    ans = X
    for i in range(N):
        ans += judge[i] * W[i]
    print(ans)