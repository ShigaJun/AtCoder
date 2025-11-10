import collections

N, K = map(int, input().split())
S = input()

c = collections.Counter(S[i:i + K] for i in range(N - K + 1))
x = max(c.values())
print(x)
ans = sorted(t for t in c.keys() if c[t] == x)
print(*ans)