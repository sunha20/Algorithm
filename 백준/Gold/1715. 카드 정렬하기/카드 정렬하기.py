import heapq
input = __import__("sys").stdin.readline

N = int(input())
hp = []

for n in range(N):
    heapq.heappush(hp, int(input()))
result = 0
while len(hp)>1:
    a = heapq.heappop(hp)
    b = heapq.heappop(hp)
    heapq.heappush(hp, a+b)
    result += a + b

print(result)