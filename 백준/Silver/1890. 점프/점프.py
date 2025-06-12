input = __import__('sys').stdin.readline

def jump(sx,sy):
    if sx == N-1 and sy == N-1:
        return 1

    if dp[sx][sy] == -1:
        now = board[sx][sy]
        dp[sx][sy] = 0
        if sx + now < N:
            dp[sx][sy] += jump(sx + board[sx][sy], sy)
        if sy + now < N:
            dp[sx][sy] += jump(sx, sy + board[sx][sy])
    return dp[sx][sy]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
print(jump(0,0))
