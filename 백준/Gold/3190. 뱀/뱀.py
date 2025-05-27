from collections import deque

input = __import__("sys").stdin.readline

N = int(input())        # 보드 크기
K = int(input())        # 사과 개수
apples = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    temp = list(map(int, input().rstrip().split()))
    apples[temp[0]][temp[1]] = 1

L = int(input())        # 뱡향 전환 횟수
dirs = [0]*10001
for _ in range(L):
    temp = list(input().rstrip().split())
    dirs[int(temp[0])] = temp[1]

snake = deque()
snake.append((1,1))
cnt = 0
x = 1
y = 2
D = [[0,1], [1, 0], [0,-1], [-1,0]]
Di = 0

while True:
    cnt += 1

    # 벽 판별
    if x < 1 or y < 1 or x > N or y > N:
        print(cnt)
        break

    # 뱀 판별
    if (x, y) in snake:
        print(cnt)
        break

    snake.append((x, y))

    if apples[x][y] == 1:      # 사과 get
        apples[x][y] = 0
    else: snake.popleft()

    if dirs[cnt] != 0:
        if dirs[cnt] == "D": Di = (Di + 1) % 4   # 오른쪽
        else: Di = (Di - 1) % 4                  # 왼쪽

    x += D[Di][0]
    y += D[Di][1]