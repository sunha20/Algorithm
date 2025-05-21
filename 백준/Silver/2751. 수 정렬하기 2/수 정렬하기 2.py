input = __import__('sys').stdin.readline
N = int(input())
k = 1000001
mlst = [0] * k
plst = [0] * k

for _ in range(N):
    num = int(input())
    if num >= 0:
        plst[num] = 1
    else:
        mlst[k + num] = 1

for i in range(len(mlst)):
    if (mlst[i] == 1):
        print(i - 1000001)

for i in range(len(plst)):
    if (plst[i] == 1):
        print(i)