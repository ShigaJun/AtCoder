N, M = map(int, input().split())
S = [input() for _ in range(N)]
S = [list(map(int, str(s))) for s in S]
results = [-1] * M
ans = [0] * N

for i in range(M):
    cnt_0 = 0
    cnt_1 = 0
    for j in range(N):
        if S[j][i] == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
    if cnt_0 == 0:
        results[i] = 1
    elif cnt_1 == 0:
        results[i] = 0
    elif cnt_0 < cnt_1:
        results[i] = 0
    else:
        results[i] = 1

for i in range(M):
    for j in range(N):
        if S[j][i] == results[i]:
            ans[j] += 1

for i in range(N):
    if ans[i] == max(ans):
        print(i + 1, end=' ')