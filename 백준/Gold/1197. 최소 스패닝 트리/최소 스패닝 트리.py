import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(n):
    if n == parentsList[n]:
        return n
    else:
        p = find_parent(parentsList[n])
        parentsList[n] = p
        return p

N, M = map(int, input().split())
parentsList = [i for i in range(N + 1)]
edgeList = []

for m in range(M):
    x, y, w = map(int, input().split())
    edgeList.append((w, x, y))
edgeList.sort()


cnt = N-1
sum = 0

for edge in edgeList:
    if cnt == 0:
        break

    w, x, y = edge

    xp = find_parent(x)
    yp = find_parent(y)

    if xp != yp:
        parentsList[xp] = min(xp,yp)
        parentsList[yp] = min(xp,yp)
        cnt -= 1
        sum += w


print(sum)