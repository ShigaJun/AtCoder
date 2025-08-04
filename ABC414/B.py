n = int(input())
c = [''] * n
l = [''] * n
for i in range(n):
    c[i], l[i] = input().split()
for i in range(n):
    l[i] = int(l[i])
if sum(l) > 100:
    print("Too Long")
else:
    ans = ""
    for i in range(n):
        for j in range(l[i]):
            ans += c[i]
    print(ans)