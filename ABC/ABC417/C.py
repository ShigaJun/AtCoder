from collections import Counter

N = int(input())
A = list(map(int, input().split()))

Ai_plus_i = Counter(A[i] + i for i in range(N))
print(sum(Ai_plus_i[j - A[j]] for j in range(N)))