input = __import__('sys').stdin.readline
N = int(input())
k = 10001
plst = [0] * k

for _ in range(N):
    plst[int(input())] += 1

for i in range(len(plst)):
    for j in range(plst[i]):
        print(i)
