N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    cnt = 0
    for i in range(N):
        if A[i] > 0:
            cnt += 1
    if cnt <= 1:
        print(ans)
        break
    A = sorted(A, reverse=True)
    A[0] -= 1
    A[1] -= 1
    ans += 1