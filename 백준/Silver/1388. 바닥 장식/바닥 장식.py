def dfs(x,y,t):
    if t == "-" and y+1 < M and floor[x][y + 1] == '-':
        visited[x][y+1] = 1
        dfs(x, y + 1, '-')

    elif t == "|" and x+1 < N and floor[x + 1][y] == '|':
        visited[x+1][y] = 1
        dfs(x + 1, y, '|')
    return

N, M = map(int,input().split())
floor = [list(input()) for _ in range(N) ]
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0

for n in range(N):
    for m in range(M):
        if visited[n][m] == 0:
            visited[n][m] = 1
            cnt += 1
            dfs(n, m, floor[n][m])

print(cnt)