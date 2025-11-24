from collections import Counter

S = list(input())
for i in range(len(S)):
    S[i] = int(S[i])
    
s = [[S[0], 1]]

cur = 0
for i in range(1, len(S)):
    if S[i] == s[cur][0]:
        s[cur][1] += 1
    else:
        cur += 1
        s.append([S[i], 1])

ans = 0
for i in range(len(s) - 1):
    if s[i + 1][0] - s[i][0] == 1:
        ans += min(s[i][1], s[i + 1][1])
print(ans)