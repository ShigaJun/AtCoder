import math

N = int(input())
W = [0] * N
H = [0] * N
B = [0] * N

l = [1] * N
hw = 0
bw = 0
hh = 0
bh = 0
mh = []

for i in range(N):
    W[i], H[i], B[i] = map(int, input().split())
    if H[i] > B[i]:
        l[i] = 0
        mh.append([H[i] - B[i], W[i]]) # [ヘッドからボディに付け替えたときに下がる嬉しさ, 重さ]
        
for i in range(N):
    if l[i] == 0:
        hw += W[i]
        hh += H[i]
    else:
        bw += W[i]
        bh += B[i]

ans = hh + bh

if hw > bw:
    mh = sorted(sorted(mh, key=lambda x: x[1]))
    i = 0
    while i < len(mh) - 2 and mh[i][1] < math.ceil((hw - bw) / 2):
        i += 1
        t1 = ans
    if mh[i][1] >= math.ceil((hw - bw) / 2):
        hw -= mh[i][1]
        bw += mh[i][1]
        t2 = ans - mh[i][0]
    ans = max(t1, t2)
print(ans)