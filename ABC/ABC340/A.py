A, B, D = map(int, input().split())

ans = [A]
while True:
    if ans[-1] == B:
        break
    ans.append(ans[-1] + D)

print(*ans)