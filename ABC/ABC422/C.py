T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    print(min(a, c, (a + b + c) // 3))