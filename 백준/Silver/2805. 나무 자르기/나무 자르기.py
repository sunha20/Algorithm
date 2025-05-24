N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
trees.sort()
hl = 0
hr = trees[-1]
while hl<hr:
    hm = (hl + hr+1) // 2
    idx = 0
    for t in range(N):
        if hm < trees[t]:
            idx = t
            break

    m = sum(trees[idx:]) - (hm*(N-idx))
    if m < M: hr = hm-1
    if m >= M: hl = hm

print(hl)