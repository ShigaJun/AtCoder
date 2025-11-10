S, A, B, X = map(int, input().split())

tmp = X // (A + B)
ans = (tmp * A + min(A, X - tmp * (A + B))) * S
print(ans)