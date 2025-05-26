import sys

def solution():
    num = int(sys.stdin.readline())
    lst = []
    sum = 0

    for i in range(num):
        val = int(sys.stdin.readline())
    
        if val:
            lst.append(val)
            sum += val
        else:
            val = lst.pop(-1)
            sum -= val
    return sum

if __name__ == "__main__":
    print(solution())

    