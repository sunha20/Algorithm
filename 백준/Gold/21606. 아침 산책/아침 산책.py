import sys

sys.setrecursionlimit(10 ** 5)
input = __import__('sys').stdin.readline

def dfs(node):
    global cnt
    for nxt in tree[node]:
        if visited[nxt] == 0:
            if loc[nxt] == "1":
                cnt += 2
            else:
                visited[nxt] = 1
                dfs(nxt)
                visited[nxt] = 0


    return


N= int(input())
loc = "0" + input()                       # 접근을 위해 앞에 1개 추가
visited = [0] * (N+1)
tree = [[] for i in range(N+1)]
cnt = 0

for _ in range(N-1):                # 인접 리스트 생성
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

for i in range(1, N+1):
    if loc[i] == "1":
        visited[i] = 1
        dfs(i)

print(cnt)
