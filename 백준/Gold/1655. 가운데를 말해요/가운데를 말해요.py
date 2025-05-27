import heapq

input = __import__("sys").stdin.readline

N = int(input())
a = int(input())
print(a)
if N == 1: exit()
    
b = int(input())
print(min(a,b))

smallMaxH = [-min(a, b)]
bigMinH = [max(a, b)]


for _ in range(N-2):
    num = int(input())

    # 삽입
    if num < -smallMaxH[0]:
        heapq.heappush(smallMaxH, -num)
    elif num > bigMinH[0]:
        heapq.heappush(bigMinH, num)
    else:
        if len(smallMaxH) < len(bigMinH):
            heapq.heappush(smallMaxH, -num)
        else: heapq.heappush(bigMinH, num)

    # 균형 맞추기
    diff = len(smallMaxH) - len(bigMinH)
    if diff == -2:
        heapq.heappush(smallMaxH, -heapq.heappop(bigMinH))
    elif diff == 2:
        heapq.heappush(bigMinH, -heapq.heappop(smallMaxH))

    diff = len(smallMaxH) - len(bigMinH)
    # 중앙값 구하기
    if diff >= 0:
        print(-smallMaxH[0])
    else:
        print(bigMinH[0])