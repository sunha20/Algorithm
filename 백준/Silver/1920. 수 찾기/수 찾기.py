N = int(input())
lst = list(map(int, input().split(" ")))
lst.sort()
M = int(input())
targets = list(map(int, input().split(" ")))

for t in targets:
    si = 0
    ei = N -1
    while si <= ei:
        mid = (si + ei) // 2
        if lst[mid] == t:
            print(1)
            break
        else:
            if lst[mid] < t: si = mid + 1
            else: ei = mid - 1
    else:
        print(0)