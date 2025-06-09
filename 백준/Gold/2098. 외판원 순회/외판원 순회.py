import sys


def dfs(start, now, visited):
    if visited == (1 << N) -1: # 다 방문
        if gp[now][start] != 0:
            return gp[now][start]
        else: return sys.maxsize

    if dp[now][visited] != -1:
        return dp[now][visited]

    m = sys.maxsize

    for next in range(N):
        if gp[now][next] != 0 and (visited & (1 << next)) == 0: # 이동 가능
            m = min(m, dfs(start, next, visited | (1 << next)) + gp[now][next])

    dp[now][visited] = m
    return m

N = int(input())
gp = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(2**N)] for _ in range(N)]
result = []
print(dfs(0, 0, 1))