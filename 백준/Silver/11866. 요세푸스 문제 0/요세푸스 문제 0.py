import sys

def solution():
    N, gap = map(int, sys.stdin.readline().rstrip().split())

    lst = [x for x in range(1, N+1)]
    idx = gap-1
    result ="<"

    while lst:
        if idx >= len(lst):
            idx %= len(lst)
        result += str(lst.pop(idx))+", "
        idx += gap-1

    print(result[:-2] +">")

if __name__ == "__main__":
    solution()
