### top down
import sys
sys.setrecursionlimit(10**6)

def findRoad(sx, sy):

    if sx == ex and sy == ey: return 1
    if dp[sx][sy] != -1: return dp[sx][sy]

    dp[sx][sy] = 0
    if sx > 0 and road[sx][sy] > road[sx - 1][sy]:
        dp[sx][sy] += findRoad(sx-1, sy)
    if sy > 0 and road[sx][sy] > road[sx][sy - 1]:
        dp[sx][sy] += findRoad(sx, sy - 1)
    if sx < ex and road[sx][sy] > road[sx + 1][sy]:
        dp[sx][sy] += findRoad(sx + 1, sy)
    if sy < ey and road[sx][sy] > road[sx][sy + 1]:
        dp[sx][sy] += findRoad(sx, sy + 1)
    return dp[sx][sy]

M, N = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
ex, ey = (M-1, N-1)
print(findRoad(0,0))