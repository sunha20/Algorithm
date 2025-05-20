def n_queen(i):
    if (i == N): return 1
    cnt = 0
    for j in range(N):
        if checkCol[j] == 0 and checkDiagAdd[i+j] == 0 and checkDiagMinus[i-j+N] == 0:
            checkCol[j] = checkDiagAdd[i+j] = checkDiagMinus[i-j+N] = 1
            cnt += n_queen(i+1)
            checkCol[j] = checkDiagAdd[i+j] = checkDiagMinus[i-j+N] = 0
    return cnt

N = int(input())
checkCol = [0] * N
checkDiagAdd = [0] * (2*N)
checkDiagMinus = [0] * (2*N)
print(n_queen(0))