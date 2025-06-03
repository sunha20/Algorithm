import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, color):
    global flag
    colors[node] = color

    for nxt in gp[node]:
        if colors[nxt] == color:
            flag = False
            return

        if colors[nxt] == 0:
           dfs(nxt, -color)


K = int(input())

for k in range(K):              # 테스트 케이스
    V, E = map(int, input().split())
    gp = [[] for _ in range(V+1)]
    colors = [0] * (V+1)
    for _ in range(E):          # 인접 리스트 만들기
        x,y = map(int, input().split())
        gp[x].append(y)
        gp[y].append(x)

    flag = True
    for v in range(1, V+1):          # 탐색
        if flag == False:
            break
        if colors[v] == 0:
            dfs(v, 1)

    if flag: print("YES")
    else: print("NO")
