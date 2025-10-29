T = int(input())

for _ in range(T):
    n = list(map(int, input().split()))
    ans = min(n[0], n[2], sum(n) // 3)
    print(ans)