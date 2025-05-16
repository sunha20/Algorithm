N, X = map(int,input().split())
Alist = input().split()

for i in range(N):
    now = int(Alist[i])
    if (now < X):
        print(now, end=" ")