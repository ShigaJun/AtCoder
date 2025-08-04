t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s = [s[0]] + sorted(s[1:-1]) + [s[-1]]
    
    ans = 2
    i = 0
    j = 0
    while j < n - 2:
        j += 1
        if s[i] * 2 >= s[-1]:
            break
        elif s[j + 1] > s[i] * 2:
            if s[j] > s[i] * 2:
                ans = -1
                break
            else:
                i = j
                ans += 1
    print(ans)