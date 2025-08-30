N = int(input())
S = input()
X = []

for i in range(2 * N):
    if S[i] == 'A':
        X.append(i)

sum_a = sum_b = 0
for k in range(N):
    sum_a += abs(X[k] - 2 * k)
    sum_b += abs(X[k] - (2 * k + 1))

ans = min(sum_a, sum_b)
print(ans)