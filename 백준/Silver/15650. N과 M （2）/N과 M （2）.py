def backtracking(i, m):
    now.append(str(i))
    if (m == 1):
        print(" ".join(now))
        return

    for j in range(i+1, N+1):
        backtracking(j, m-1)
        now.pop()
    return

N,M = map(int,input().split())

for i in range(1, N+1):
    now = []
    backtracking(i, M)