import sys

def fibonacci():
    N = int(sys.stdin.readline().rstrip())
    dp_0 = [1,0,1]
    dp_1 = [0,1,1]
    while N > 0:
        N -= 1
        num = int(sys.stdin.readline().rstrip())
        if (num < len(dp_0)):
            print(dp_0[num], dp_1[num])
        else:
            zero = 0
            one = 0
            for i in range(len(dp_0), num+1):
                dp_0.append(dp_0[i - 1] + dp_0[i - 2])
                dp_1.append(dp_1[i - 1] + dp_1[i - 2])
                zero = dp_0[i]
                one = dp_1[i]
            print(zero, one)


if __name__ == "__main__":
    fibonacci()