def solve():
    N = int(input())
    S = list(map(int, input().split()))
    cur = S[0]
    goal = S[-1]
    S = sorted(S[1:-1])
    ans = 2

    for i in range(len(S)):
        if goal <= cur * 2:
            break
        if S[i] <= cur * 2 and (i == len(S) - 1 or S[i + 1] > cur * 2):
            ans += 1
            cur = S[i]
        if S[i] > cur * 2:
            break

    if goal > cur * 2:
        print(-1)
    else:
        print(ans)
    return

for _ in range(int(input())):
    solve()