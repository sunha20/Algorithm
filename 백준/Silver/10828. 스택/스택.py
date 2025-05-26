import sys

N = int(input())

stack = []
top = None
size = 0

while N > 0:
    N -= 1

    instruction = sys.stdin.readline()

    if "push" in instruction:
        val = int(instruction[5:])
        
        stack.append(val)
        size += 1
        top = val
    elif "pop" in instruction:
        if size > 1:
            print(stack.pop(-1))
            size -= 1
            top = stack[-1]
        elif size == 1:
            print(stack.pop(-1))
            size = 0
            top = None
        else:
            print(-1)

    elif "size" in instruction:
        print(size)
    elif "empty" in instruction:
        if size == 0:
            print(1)
        else:
            print(0)
    elif "top":
        if size == 0:
            print(-1)
        else:
            print(top)
