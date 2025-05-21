def tsp(start, now, move, cost):
    if (move == 1):
        if (lst[now][start] != 0):
            costs.append(cost+lst[now][start])
            return

    visited[now] = 1

    for next in range(N):
        if visited[next] == 0 and lst[now][next] != 0:
            tsp(start,next, move-1, cost+ lst[now][next])
    visited[now] = 0
    return


N = int(input())
lst = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [0] * N
costs = []

for i in range(N):
    tsp(i, i, N, 0)

print(min(costs))
