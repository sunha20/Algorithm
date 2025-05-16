import math

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for n in nums:
    if n == 1: cnt -= 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            break
    else:
        cnt += 1

print(cnt)