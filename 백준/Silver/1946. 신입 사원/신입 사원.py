input = __import__("sys").stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(N):
        x, y = map(int, input().split())
        lst[x] = y
    a = lst[1]
    cnt = 1
    for i in range(2, N+1):
        if lst[i] < a:
            cnt += 1
            a = lst[i]
    print(cnt)