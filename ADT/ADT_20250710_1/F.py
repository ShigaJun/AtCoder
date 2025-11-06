n, t = input().split()
ans = []
for i in range(int(n)):
    s = input()
    if len(t) == len(s):
        cnt = 0
        for j in range(len(t)):
            if t[j] != s[j]:
                cnt += 1
        if cnt <= 1:
            ans.append(i)
    elif abs(len(t) - len(s)) == 1:
        j = 0
        k = 0
        while j != len(t) - 1 and k != len(s) - 1:
            if t[j] != s[j]:
                cnt += 1
print(*ans)