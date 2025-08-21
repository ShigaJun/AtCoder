S = input()
T = input()

def rle(s):
    ans = []
    for c in s:
        if ans and ans[-1][0] == c:
            ans[-1][1] += 1
        else:
            ans.append([c, 1])
    return ans

s_rle = rle(S)
t_rle = rle(T)

if len(s_rle) != len(t_rle):
    print("No")
    exit()
for si, ti in zip(s_rle, t_rle):
    if si[0] != ti[0] or ti[1] < si[1] or (ti[1] > si[1] and si[1] == 1):
        print("No")
        break
else:
    print("Yes")