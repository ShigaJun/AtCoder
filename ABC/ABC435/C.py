N = int(input())
A = list(map(int, input().split()))

cnt = A[0] - 1
for i in range(1, N):
    if cnt == 0:
        print(i)
        exit()
    cnt = max(cnt - 1,  A[i] - 1)
print(N)