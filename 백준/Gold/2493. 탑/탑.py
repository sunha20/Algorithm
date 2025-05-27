from collections import deque
N = int(input())
buildings = list(map(int, input().split()))
checkB = deque()
checkB.append([0, buildings[0]])
receivers = [0]*N

for i in range(1, N):
    while True:
        if len(checkB) == 0:
            receivers[i] = 0
            break

        now = buildings[i]
        last = checkB[-1]
        if now >= last[1]:
            checkB.pop()
        else:
            receivers[i] = last[0] + 1
            break
    checkB.append([i, buildings[i]])

print(*receivers)