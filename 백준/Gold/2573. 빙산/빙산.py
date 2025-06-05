from collections import deque

def melt_ice(x, y):
    global meltedIce, iceCnt

    iceCnt += 1
    visited[(x,y)] = year   # 해당 연도에 방문
    que = deque()
    que.append((x,y))

    while len(que) > 0:
        nowX, nowY = que.popleft()
        # 탐색 (얼음 녹이기, 연결된 빙산으로 넘어가기)
        for i in range(4):
            newX = nowX + ix[i]
            newY = nowY + iy[i]
            if (0 <= newX < N) and (0 <= newY < M):
                if -year < world[newX][newY] <= 0:
                    world[nowX][nowY] -= 1
                else:
                    if (newX, newY) not in visited or visited[(newX, newY)] < year:
                        iceCnt += 1
                        visited[(newX, newY)] = year  # 해당 연도에 방문
                        que.append((newX, newY))
        if world[nowX][nowY] <= 0:
            meltedIce += 1
            world[nowX][nowY] = -year
    return



N, M = map(int, input().split())

def find_ice():
    for r in range(1, N - 1):
        for c in range(1, M - 1):
            if world[r][c] > 0:
                return r, c
    return None


world = [list(map(int, input().split())) for _ in range(N)]
visited = dict()
ix = [0,1,0,-1]
iy = [1,0,-1,0]

ice = 0
for r in range(1, N-1):
    for c in range(1, M-1):
        if world[r][c] != 0:
            ice += 1

iceCnt = ice
meltedIce = 0
year = 0

while True:
    ice = iceCnt - meltedIce
    iceCnt = 0
    meltedIce = 0
    year += 1

    x, y = find_ice()
    melt_ice(x,y)

    # 탐색하고 보니 사실 저번 연도에 분리됨.
    if iceCnt != ice:
        print(year-1)
        exit()
    
    # 다 녹음
    if iceCnt - meltedIce == 0:
        print(0)
        exit()