H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
visited = [[0] * W for _ in range(H)]

def bfs(si, sj):
    ok = True
    q = [(si, sj)]
    visited[si][sj] = 1
    for i, j in q:
        if i == 0 or i == H-1 or j == 0 or j == W-1:
            ok = False
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii = i + di
            jj = j + dj
            if 0 <= ii < H and 0 <= jj < W and S[ii][jj] == '.' and visited[ii][jj] == 0:
                visited[ii][jj] = 1
                q.append((ii, jj))
    return ok
    
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and visited[i][j] == 0:
            if bfs(i, j):
                ans += 1
print(ans)