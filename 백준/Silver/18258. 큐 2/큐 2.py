input = __import__('sys').stdin.readline

stk = [0]*2000000
size = 0
front = 0
back = -1

N = int(input())
for _ in range(N):
    inst = list(input().strip().split())

    if inst[0] == "push":
        back += 1
        size += 1
        stk[back] = int(inst[1])
    elif inst[0] == "pop":
        if size > 0:
            print(stk[front])
            size -= 1
            front += 1
        else:
            print(-1)
    elif inst[0] == "size":
        print(size)
    elif inst[0] == "empty":
        if size == 0: print(1)
        else: print(0)
    elif inst[0] == "front":
        if size > 0:
            print(stk[front])
        else:
            print(-1)
    elif inst[0] == "back":
        if size > 0:
            print(stk[back])
        else:
            print(-1)