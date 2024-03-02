import sys, heapq


def max_heap():
    N = int(sys.stdin.readline().rstrip())
    heap = []

    while N > 0:
        N -= 1
        x = int(sys.stdin.readline().rstrip())

        if x != 0:
            heapq.heappush(heap, -x)

        else:
            if len(heap) != 0:
                print(-heapq.heappop(heap))
            else:
                print(0)

if __name__ == "__main__":
    max_heap()