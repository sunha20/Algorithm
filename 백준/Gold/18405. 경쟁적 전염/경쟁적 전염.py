import heapq

N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

if virus[X][Y] != 0:
    print(virus[X][Y])
    exit()

time = 0
que = []

for x in range(N):
    for y in range(N):
        if virus[x][y] != 0:
            heapq.heappush(que, [time, virus[x][y], x, y])

ix = [0,-1,0,1]
iy = [-1,0,1,0]
while len(que) > 0:
    t, v, cx, cy = heapq.heappop(que)

    if t >= S: # 시간 초과
        break

    for i in range(4):
        nx = cx + ix[i]
        ny = cy + iy[i]
        if 0 <= nx < N and 0 <= ny < N and virus[nx][ny] == 0:
            virus[nx][ny] = v
            if nx == X and ny == Y:
                break

            heapq.heappush(que, [t+1, virus[nx][ny], nx, ny])
print(virus[X][Y])