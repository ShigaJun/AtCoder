q = int(input())
a = []
head = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a.append([query[2],  query[1]])
    else:
        k = query[1]
        ans = 0
        while k > 0:
            if a[head][1] <= k:
                k -= a[head][1]
                ans += a[head][0] * a[head][1]
                head += 1
            else:
                ans += a[head][0] * k
                a[head][1] -= k
                k = 0
        print(ans)