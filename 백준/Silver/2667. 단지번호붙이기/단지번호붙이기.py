from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())

house = []

for _ in range(n):
    temp = list(map(int, input().strip()))
    house.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([[x, y]])
    house[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if house[nx][ny] == 1:
                    queue.append([nx, ny])
                    house[nx][ny] = 0
                    cnt += 1
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            count.append(bfs(i, j))
count.sort()

print(len(count))
for i in range(len(count)):
    print(count[i])