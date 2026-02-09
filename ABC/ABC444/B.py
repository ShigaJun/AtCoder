N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    n = str(i)
    tmp = 0
    for j in range(len(n)):
        tmp += int(n[j])
    if tmp == K:
        ans += 1
print(ans)