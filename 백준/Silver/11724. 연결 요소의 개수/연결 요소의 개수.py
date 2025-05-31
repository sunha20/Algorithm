import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

input = __import__('sys').stdin.readline

def dfs(node):
    for nxt in range(1, N + 1):
        if gp[node][nxt] == 1 and visited[nxt] != 1:
            visited[nxt] = 1
            dfs(nxt)
    return

def bfs(node):
    que = deque()
    que.append(node)
    visited[node] = 1
    while len(que) > 0:
        now = que.popleft()
        for next in range(1, N + 1):
            if gp[now][next] == 1 and visited[next] != 1:
                visited[next] = 1
                que.append(next)
    return

N, M= map(int, input().split())
gp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int,input().split())
    gp[x][y] = 1
    gp[y][x] = 1

visited = [0] * (N+1)
cnt = 0
for n in range(1, N + 1):
    if visited[n] == 0:
        visited[n] = 1
        # dfs(n)
        bfs(n)
        cnt += 1
print(cnt)
