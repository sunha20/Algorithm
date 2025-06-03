import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def printT(start, end):
    if start > end:
        return
    root = preTree[start]
    if start == end:
        print(root)
        return

    mid = end+1
    for i in range(start+1, end+1):
        if preTree[i] > root:
            mid = i
            break
    # left
    printT(start+1, mid - 1)
    # right
    printT(mid, end)
    print(root)
    return

V = int(input())
preTree = [V]
while True:
    try:
        preTree.append(int(input()))
    except:
        break

printT(0, len(preTree)-1)