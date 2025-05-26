import sys        
            
def solution():   
    N = int(sys.stdin.readline().rstrip())
    queue = [2*(i+1) for i in range(N//2)]
    point = 0
    
    if N == 1:
        return 1

    if N%2 == 1:
        card = queue[point]
        queue.append(card)
        point = 1

    N //= 2 
    while N > 1:
        card = queue[point + 1]
        queue.append(card)
        N -= 1
        point += 2
    return queue[point]

if __name__ == "__main__":
    print(solution())