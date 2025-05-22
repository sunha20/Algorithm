from itertools import combinations

N, S = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))
cnt = 0

for i in range(1, N+1):
    for subset in combinations(lst, i):
        if sum(subset) == S: cnt += 1

print(cnt)