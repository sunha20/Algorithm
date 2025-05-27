import sys
N = int(input())
lst = list(map(int, input().split()))
lst.sort()

s = 0
e = N-1
minMix = sys.maxsize
minIdx = (0,0)
while s<e:
    newMix = lst[s] + lst[e]
    if newMix == 0:
        print(lst[s], lst[e])
        break
    if abs(newMix) < minMix:
        minMix = abs(newMix)
        minIdx = (s, e)

    if newMix < 0:
        s += 1
    else:
        e -= 1
else:
    print(lst[minIdx[0]], lst[minIdx[1]])

