import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = __import__('sys').stdin.readline

def dfs(node):
    for nxt in gp[node]:
        if parentList[nxt] == 0:
            parentList[nxt] = node
            dfs(nxt)
    return

def bfs(node):
    que = deque()
    que.append(node)
    parentList[node] = -1
    while len(que) > 0:
        now = que.popleft()
        for next in gp[now]:
            if parentList[next] == 0:
                parentList[next] = now
                que.append(next)
    return

N= int(input())
gp = [[] for _ in range(N + 1)]
parentList = [0 for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int,input().split())
    gp[x].append(y)
    gp[y].append(x)

# dfs(1)
bfs(1)
for i in range(2, len(parentList)):
    print(parentList[i])