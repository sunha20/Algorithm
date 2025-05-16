N, X = map(int,input().split())
Alist = map(int, input().split())

for _ in range(N):
    now = next(Alist)
    if (now < X):
        print(now, end=" ")