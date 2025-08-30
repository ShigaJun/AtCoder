N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

pt = [0] * N # それぞれの人のポイントを格納した配列 [0, 0, 0]
for j in range(M):
    cnt_0 = cnt_1 = 0
    for i in range(N):
        if S[i][j] == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
    # 点数追加
    for i in range(N):
        if S[i][j] == '0':
            if cnt_0 < cnt_1:
                pt[i] += 1
        else:
            if cnt_0 > cnt_1:
                pt[i] += 1
    high = max(pt)
    ans = [str(i + 1) for i in range(N) if pt[i] == high]
print(" ".join(ans))