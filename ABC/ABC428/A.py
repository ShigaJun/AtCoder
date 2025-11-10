S, A, B, X = map(int, input().split())

ans = (X // (A + B) * A + min(A, X % (A + B))) * S
print(ans)