from collections import deque
N, M = map(int, input().split())
gp = [ [0,[]] for _ in range(N+1)]       # 징입 / 진출

for i in range(M):
    x, y = map(int, input().split())
    gp[y][0] += 1
    gp[x][1].append(y)

que = deque()
resultList = []
for i in range(1, N+1):
    if gp[i][0] == 0:
        que.append(i)

while len(que) > 0:
    now = que.popleft()
    resultList.append(now)
    for nxt in gp[now][1]:
        gp[nxt][0] -= 1
        if gp[nxt][0] == 0:
            que.append(nxt)

print(*resultList)