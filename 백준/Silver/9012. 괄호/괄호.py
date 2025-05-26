import sys
def solution():
    cnt = 0
    ps = sys.stdin.readline().rstrip()
    for i in ps:
        if i == ")":
            cnt -= 1
            if cnt < 0:
                break
        else:
            cnt += 1
    if cnt == 0:
        return "YES"
    else:
        return "NO"
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    while N != 0:
        N-=1
        print(solution())