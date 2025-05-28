def dq(b):
    if b == 1:
        return A
    a = dq(b//2)
    r = matrix_mul(a,a)
    if b % 2 == 0:
        return r
    else:
        return matrix_mul(r, A)

def matrix_mul(a, c):
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (a[i][k] * c[k][j]) %1000
            result[i][j] %= 1000
    return result

N, B = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
D = dq(B)

for i in A:
    for j in range(N):
        i[j] = i[j]%1000

for i in range(N):
    print(*D[i])