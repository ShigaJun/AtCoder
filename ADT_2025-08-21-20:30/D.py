import itertools

n = int(input())
s = list(map(int, input().split()))

ans = 0
for i in range(n):
    for a, b in itertools.product(range(1, 1001), repeat=2):
        if 4 * a * b + 3 * a + 3 * b == s[i]:
            break
    else:
        ans += 1
print(ans)