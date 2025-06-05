from collections import deque

def bfs(sx,sy):
    cnt = 1
    que = deque()
    que.append((sx, sy))

    while len(que) > 0:
        x, y = que.popleft()

        for i in range(4):
            newX = x+ix[i]
            newY = y+iy[i]
            if 0 <= newX < N and 0 <= newY < N and homes[newX][newY] == "1":
                homes[newX][newY] = "0"
                cnt+=1
                que.append((newX,newY))

    return cnt

N = int(input())
homes = [list(input()) for _ in range(N)]
groupCnt = 0
homeCnt = []
ix = [0,-1,0,1]
iy = [-1,0,1,0]

for x in range(N):
    for y in range(N):
        if homes[x][y] == "1":
            homes[x][y] = "0"           # visit 처리
            groupCnt += 1
            homeCnt.append(bfs(x,y))

homeCnt.sort()
print(groupCnt)
for i in range(groupCnt):
    print(homeCnt[i])
