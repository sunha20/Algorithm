import sys

def atm():
    N = int(sys.stdin.readline().rstrip())
    P = list(map(int,sys.stdin.readline().split()))
    time = 0

    P.sort()

    for i in range(N):
        time += P[i]*(N-i)

    print(time)


if __name__ == "__main__":
    atm()