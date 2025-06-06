T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):     # coin 종류
        for j in range(1, M+1): # 금액 limit
            if j >= coins[i-1]: use = dp[i][j - coins[i-1]]     # coins[i]를 사용하는 경우
            else: use = 0
            not_use = dp[i-1][j]                                # coins[i]를 사용하지 않는 경우
            dp[i][j] = use+not_use

    print(dp[N][M])