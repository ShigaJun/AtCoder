def solve(A):
    L = min(A) + max(A)
    for i in range(1, int(len(A) / 2)):
        if A[i] + A[-(i + 1)] != L:
            return False
    else:
        return True

N = int(input())
A = sorted(list(map(int, input().split())))
ans = []

if N % 2 == 1:
    ans.append(max(A))
else:
    if solve(A): ans.append(min(A) + max(A))
    L = max(A)
    A = [a for a in A if a != L]
    if len(A) % 2 == 0:
        if len(A) == 0 or (solve(A) and min(A) + max(A) == L):
            ans.append(L)
print(*sorted(ans))