def n_queen(i):
    if (i == N): return 1
    cnt = 0
    for j in range(N):
        if checkCol[j] == False and checkDiagAdd[i+j] == False and checkDiagMinus[i-j+N] == False:
            checkCol[j] = checkDiagAdd[i+j] = checkDiagMinus[i-j+N] = True
            cnt += n_queen(i+1)
            checkCol[j] = checkDiagAdd[i+j] = checkDiagMinus[i-j+N] = False
    return cnt

N = int(input())
checkCol = [False] * N
checkDiagAdd = [False] * (2*N)
checkDiagMinus = [False] * (2*N)
print(n_queen(0))