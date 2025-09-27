N = int(input())
ans = 0

for i in range(1, N + 1):
    ans += pow(-1, i) * pow(i, 3)
print(ans)