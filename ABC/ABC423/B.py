N = int(input())
L = list(map(int, input().split()))

i = 0
while L[i] == 0 and i < N - 1:
    i += 1

j = 0
while L[N - 1 - j] == 0 and j < N - 1:
    j += 1

ans = max(N + 1 - (i + 1) - (j + 1), 0)
print(ans)

# visited = [0] + [1] * (N - 1) + [0]

# i = 0
# while L[i] == 0 or i < N - 1:
#     i += 1
#     visited[i + 1] = 0
#     print(visited)

# j = 1
# while L[N - j] == 0 or j < N:
#     j += 1
#     visited[N - j + 1] = 0
#     print(visited)

# ans = sum(visited)
# print(ans)