input = __import__("sys").stdin.readline
N = int(input())
numList = list(map(int, input().split()))

dp = [[1 for _ in range(N)] for _ in range(N)]
for length in range(N):
    for s in range(0, N-1):
        e = length + s
        if e >= N: break
        dp[s][e] = int(dp[s + 1][e - 1] and numList[s] == numList[e])

M = int(input())
while M > 0:
    M-=1
    s, e = map(int, input().split())
    print(dp[s-1][e-1])