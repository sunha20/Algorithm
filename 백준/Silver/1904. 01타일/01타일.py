import sys

def zero_one():
    N = int(sys.stdin.readline().rstrip())
    dp = [1, 2]

    for i in range(2,N):
        dp.append((dp[i-2] + dp[i-1])%15746)

    print(dp[N-1])

if __name__ == "__main__":
    zero_one()
