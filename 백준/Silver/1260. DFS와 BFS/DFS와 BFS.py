"""
# 완전이진 트리가 아니기 때문에 인덱스를 계산해서 사용하는 건 안 됨.
# 왼쪽 자식인지 오른쪽 자식인지 확인해야하기 때문에 그냥 안 넣으면 안되고, 어느자리가 비었는지 확인할 수 있어야함.

def preDfs(node):
    if node < 0:
        return

    preResult.append(chr(node+bias))
    preDfs(bt[node][0])
    preDfs(bt[node][1])

def inDfs(node):
    if node < 0:
        return

    inDfs(bt[node][0])
    inResult.append(chr(node + bias))
    inDfs(bt[node][1])

def postDfs(node):
    if node < 0:
        return
    postDfs(bt[node][0])
    postDfs(bt[node][1])
    postResult.append(chr(node + bias))

bias = 65
N = int(input())
bt = [[] for _ in range(N+1)]
preResult = []
inResult = []
postResult = []


for i in range(1, N + 1):
    idx, ch1, ch2 = map(ord, input().split())
    idx -= bias
    bt[idx].append(ch1 - bias)
    bt[idx].append(ch2 - bias)


preDfs(0)
inDfs(0)
postDfs(0)
print("".join(preResult))
print("".join(inResult))
print("".join(postResult))
"""
from collections import deque
def dfs(node):
    visitedDfs[node] = 1
    resultDfs.append(node)
    for next in range(1, N+1):
        if gp[node][next] == 1 and visitedDfs[next] != 1:
            dfs(next)
    return

def bfs():
    que = deque()
    que.append(V)
    visitedBfs[V] = 1
    while len(que) > 0:
        now = que.popleft()
        resultBfs.append(now)
        for next in range(1, N + 1):
            if gp[now][next] == 1 and visitedBfs[next] != 1:
                visitedBfs[next] = 1
                que.append(next)
    return


N, M, V = map(int, input().split())
gp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int,input().split())
    gp[x][y] = 1
    gp[y][x] = 1

### dfs
visitedDfs = [0 for _ in range(N + 1)]
resultDfs = []
dfs(V)
print(*resultDfs)

### bfs
visitedBfs = [0 for _ in range(N + 1)]
resultBfs = []
bfs()
print(*resultBfs)

