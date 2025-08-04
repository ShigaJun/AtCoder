grid = [[0] * 15 for _ in range(15)]
for i in range(13, 0, -2):
    for j in range(int((15 - i) / 2), int((15 - i) / 2) + i):
        for k in range(int((15 - i) / 2), int((15 - i) / 2) + i):
            if i % 4 == 3:
                grid[j][k] = 0
            else:
                grid[j][k] = 1

# for i in range(15):
#     print(grid[i])

r, c = map(int, input().split())
if grid[r - 1][c - 1] == 0:
    print("black")
else:
    print("white")