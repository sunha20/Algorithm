import sys

def printque():
    N = int(sys.stdin.readline().rstrip())

    for i in range(N):
        num, idx = map(int, sys.stdin.readline().split())
        que = list(map(int, sys.stdin.readline().split()))
        result(que, idx)


def result(que, target):
    cnt = 0
    flag = 0
    M = max(que)

    while True:
        if que[flag] == M and que[flag] != -1:
            cnt += 1
            if target == flag:
                print(cnt)
                break
            que[flag] = -1
            M = max(que)

        flag = (flag+1)% len(que)

    return

if __name__ == "__main__":
    printque()