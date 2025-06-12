import heapq

input = __import__('sys').stdin.readline
N = int(input())
lecture = []
for _ in range(N):
    i, s, e = map(int, input().split())
    lecture.append([s,[e,i]])
lecture.sort()

ing = [lecture[0][1]]
result = [0]*(N+1)
result[lecture[0][1][1]] = 1
maxLen = 1
for i in range(1,N):
    nowL = lecture[i][1][1]
    if ing[0][0] <= lecture[i][0]:
        lastL = heapq.heappop(ing)[1]
        result[nowL] = result[lastL]
    else:
        maxLen += 1
        result[nowL] = maxLen
    heapq.heappush(ing, lecture[i][1])

print(maxLen)
for i in range(1, N+1):
    print(result[i])