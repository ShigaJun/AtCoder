T = int(input())
for _ in range(T):
    N = int(input())
    tonakai = [[0, 0] for _ in range(N)]
    for i in range(N):
        tonakai[i] = list(map(int, input().split()))
    Tw = sorted(tonakai)
    Tp = sorted(tonakai, reverse=True, key=lambda x: x[1])
    # とりあえず W と P でそれぞれソートしてみる
    # 最初トナカイは全員ソリに乗っているものと考える
    # そこから 1 匹ずつ降ろして行くのが貪欲法．もちろん間に合わない
    # DP ですか...？
    # 最大容量とかいう概念はないから，少なくとも単純なナップサック問題ではないよね
    # そもそも本当に DP で解く問題なのかどうかもわかんないけど
    # ん...？全通り（2^N）試しても間に合うくね？ -> やっぱ無理そ
    # sum(W) >= sum(P) とき，ans = 0
    # if sum(W) >= sum(P):
    #     print(0)
    #     continue
    # l = [[int(bit) for bit in format(i, 'b').zfill(N)] for i in range(2**N)]
    ans1 = 0
    sum_w = sum(t[0] for t in tonakai)
    sum_p = 0
    for i in range(N):
        sum_w -= Tw[i][0]
        sum_p += Tw[i][1]
        ans1 += 1
        if sum_w <= sum_p:
            break
    ans2 = 0
    sum_w = sum(t[0] for t in tonakai)
    sum_p = 0
    for i in range(N):
        sum_w -= Tp[i][0]
        sum_p += Tp[i][1]
        ans2 += 1
        if sum_w <= sum_p:
            break
    print(N - min(ans1, ans2))