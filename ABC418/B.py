s = input()
ans = 0
for i in range(len(s) - 2):
    for j in range(len(s) - 1, i + 1, -1):
        if s[i] == s[j] == 't':
            x = 0
            len_t = 0
            for k in range(i, j + 1):
                if s[k] == 't':
                    x += 1
                len_t += 1
            p = (x - 2) / (len_t - 2)
            if p >= ans:
                ans = p
print(ans)