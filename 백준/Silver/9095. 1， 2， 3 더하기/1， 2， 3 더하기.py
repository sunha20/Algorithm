def add123(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return add123(n-1) + add123(n-2) + add123(n-3)

T = int(input())
for t in range(T):
    print(add123(int(input())))