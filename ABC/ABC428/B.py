import collections

N, K = map(int, input().split())
S = input()

l = []

for i in range(N - K + 1):
    l.append(S[i:i + K])
l = sorted(l)
c = collections.Counter(l)
x = max(c.values())
print(x)
for t in c.keys():
    if c[t] == x:
        print(t, end=' ')