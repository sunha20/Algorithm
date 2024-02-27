import sys
def solution(n, r, j):
    result = 1
    
    while n > j:
        result *= n
        n -= 1
    
    b = 1
   
    for i in range(1,r+1):
        b *= i
    
    print(int(result/b))
    
    
if __name__=="__main__":
    cnt = int(sys.stdin.readline().rstrip())

    while cnt > 0:
        N, M = map(int, sys.stdin.readline().rstrip().split())
        solution(M,N, M-N)
        cnt -= 1
        