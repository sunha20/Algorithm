def Z(n, r, c):
    global cnt

    if r == R and c == C:
        print(cnt)
        exit()

    i = 2**(n-1)
    if (r <= R < r+i) and (c <= C < c+i):       # 1사분면
        Z(n - 1, r, c)
    else: cnt += (i*i)

    if (r <= R < r+i) and (c+i <= C < c+(2*i)):       # 2사분면
        Z(n - 1, r, c + i)
    else: cnt += (i*i)

    if (r+i <= R < r+(2*i)) and (c <= C < c+i):       # 3사분면
        Z(n - 1, r + i, c)
    else: cnt += (i*i)

    if (r+i <= R < r+(2*i)) and (c+i <= C < c+(2*i)):       # 4사분면
        Z(n - 1, r + i, c + i)
    else: cnt += (i*i)
    return


N, R, C = map(int, input().split())     # 2의 N승
cnt = 0
Z(N, 0, 0)