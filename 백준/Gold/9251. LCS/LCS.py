import sys
sys.setrecursionlimit(10**6)

def lcs(s1, s2):
    if s1 >= l1 or s2 >= l2:
        return 0

    if dp[s1][s2] >= 0:
        return dp[s1][s2]

    if str1[s1] == str2[s2]:
        dp[s1][s2] = lcs(s1+1, s2+1) + 1
    else:
        dp[s1][s2] = max(lcs(s1+1, s2), lcs(s1, s2+1))

    return dp[s1][s2]

str1 = input()
str2 = input()
l1 = len(str1)
l2 = len(str2)
dp = [[-1 for _ in range(l2)] for _ in range(l1)]

print(lcs(0,0))