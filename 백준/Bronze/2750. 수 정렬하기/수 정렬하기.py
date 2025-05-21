N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(input())

lst.sort()

for x in lst:
    print(x)