input = __import__("sys").stdin.readline

M, N, L = map(int, input().split())
guns = list(map(int, input().split()))
guns.sort()

yList = [0] * (guns[-1] + L + 1)

for g in guns:
    for l in range(1, L):
        yList[g] = L
        if (g - 1 > 0) and (yList[g - l] < L - l):
            yList[g - l] = L - l
        else: break
    for l in range(1, L):
        if yList[g + l] < L - l:
            yList[g + l] = L - l
        else: break

cnt = 0
for _ in range(N):
    x,y = map(int, input().split())
    if yList[x] >=  y:
        cnt += 1
print(cnt)