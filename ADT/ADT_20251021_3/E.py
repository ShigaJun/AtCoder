N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

newS = [[] for _ in range(M)]

for i in range(N):
    newS[C[i] - 1].append(S[i])

cnt = [0] * M
ans = []
for i in range(N):
    if cnt[C[i] - 1] == 0:
        ans.append(newS[C[i] - 1][len(newS[C[i] - 1]) - 1])
    else:
        ans.append(newS[C[i] - 1][cnt[C[i] - 1] - 1])
    cnt[C[i] - 1] += 1
print(''.join(ans))