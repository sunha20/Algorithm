from itertools import permutations

N = int(input())
numList = list(map(int, input().split(" ")))
calList = [[] for _ in range(N-1)]

max = 0
# 순열 구하기
for per in permutations(numList, N):
    total = 0
    for i in range(N-1):
        total += abs(per[i] - per[i+1])
    if total > max: max = total

print(max)