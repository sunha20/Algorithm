# 안전지대
# https://www.acmicpc.net/problem/2468

from collections import deque

def safe(h):            # h: 가준 물 높이 /
    que = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if visited[i][j] == 0 and lst[i][j] > h:
                waterCnt[h] += 1
                visited[i][j] = 1
                que.append((i,j))

                while que:
                    node = que.popleft()
                    x = node[0]
                    y = node[1]
                    for a in A:
                        nx = x+a[0]
                        ny = y+a[1]
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 and lst[nx][ny] > h:
                            visited[nx][ny] = 1
                            que.append((nx,ny))


input = __import__('sys').stdin.readline
N = int(input())
A = [[-1, 0], [1, 0], [0, -1], [0, 1]]
lst = [list(map(int, input().split(" "))) for _ in range(N)]
waterCnt = [-1]*101


waterCnt[0] = 1
waterCnt[100] = 0

for i in range(N):
    for j in range(N):
        h = lst[i][j]
        if waterCnt[h] == -1:
            waterCnt[h] += 1
            safe(h)
safe(100)
print(max(waterCnt))