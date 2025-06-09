input = __import__("sys").stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort()
    a = lst[0][1]
    cnt = 1
    for i in range(1, N):
        if lst[i][1] < a:
            cnt += 1
            a = lst[i][1]
    print(cnt)