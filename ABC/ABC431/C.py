N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H = sorted(H)
B = sorted(B)

cnt = 0
j = 0
for i in range(N):
    if j >= M:
        break
    while j < M - 1 and H[i] > B[j]:
        j += 1
    if H[i] <= B[j]:
        cnt += 1
        j += 1
if cnt >= K:
    print("Yes")
else:
    print("No")