import sys

def coin_0():
    N, total = map(int, sys.stdin.readline().split())
    coin = []
    now = 0
    cnt = 0

    for _ in range(N):
        coin.append(int(sys.stdin.readline().rstrip()))

    for v in reversed(coin):
        temp = (total - now) // v
        cnt += temp
        now += v * temp

        if now == total:
            print(cnt)
            break

if __name__ == "__main__":
    coin_0()
