str1 = input()
str2 = input()
l1 = len(str1)
l2 = len(str2)
dp = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
dp[0] = [0 for _ in range(l2+1)]
for i in range(l1+1):
    dp[i][0] = 0

# 이해가 쉽게 앞에서 부터 쌓아가자.
# lcs(n1, n2) = max(lcs(n1-1, n2-1) + 1, lcs(n1-1,n2), lcs(n1, n2-1))
for n1 in range(1, l1+1):
    for n2 in range(1, l2+1):
        if str1[n1-1] == str2[n2-1]:
            dp[n1][n2] = dp[n1-1][n2-1] + 1
        else:
            dp[n1][n2] = max(dp[n1-1][n2], dp[n1][n2-1])
print(dp[l1][l2])
