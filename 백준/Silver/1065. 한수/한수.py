import sys


def solution():
    x = int(sys.stdin.readline().rstrip())

    if x <= 99:
        return(x)
    
    n = 10
    d = -1
    a_1 = 0
    result = 99
    i = 1
    
    while n < x//(10**i):
        if a_1+d >= 0 and a_1+d<=9:
            result+=1
        n+=1
        if n == 100:
            n = 10
            flag = x//100
            i = 2
        d = ((n%10) - (n//10))*i
        a_1 = n%10

    n_str = str(n)

    if a_1+d >= 0 and a_1+d<=9:
        for j in range(1,i+1):
            d = ((n%10) - (n//10))*j        
            n_str += str((d*j)+a_1)

        if int(n_str) <= x:
            result+=1

    return result  

if __name__ == "__main__":
    print(solution())