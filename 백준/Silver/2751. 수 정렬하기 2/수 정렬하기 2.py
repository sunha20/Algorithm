import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    
    positive = [0 for _ in range(1000001)]
    negative = positive[0:]

    while N > 0:
        N-=1
        num = int(sys.stdin.readline().rstrip())
        if num >= 0:
            positive[num] = 1
        else:
            negative[-num] = 1
    
    for i in reversed(range(1000001)):
        if negative[i] == 1:
            print(-i)

    for i in range(1000001):
        if positive[i] == 1:
            print(i)



if __name__ == "__main__":
    solution()