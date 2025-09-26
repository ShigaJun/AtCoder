N, L, R = map(int, input().split())
A = [a for a in range(1, N + 1)]
ans = A[:L-1] + list(reversed(A[L-1:R])) + A[R:]
print(*ans)