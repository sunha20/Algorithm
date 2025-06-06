"""
### bottom-up
### 작은 문제부터 큰문제로 쌓아 올림.
N = int(input())
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
"""

### top-down
### 큰 문제를 작은 문제로 재귀 호출
### 그 작은 문제가 이미 계산 한 문제면 가지고 옴

def fib(n):
    if dp[n-1] == -1:
        dp[n-1] = fib(n-1)
    if dp[n-2] == -1:
        dp[n-2] = fib(n-2)
    return dp[n-1] + dp[n-2]

N = int(input())
dp = [-1] * (N+1)
dp[0] = 0
dp[1] = 1

print(fib(N))