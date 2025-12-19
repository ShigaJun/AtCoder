S = list(input())
cnt_c = 0
cnt_s = 0
for i in range(len(S)):
    if ord('A') <= ord(S[i]) <= ord('Z'):
        cnt_c += 1
    else:
        cnt_s += 1
if cnt_c > cnt_s:
    print(''.join(S).upper())
else:
    print(''.join(S).lower())