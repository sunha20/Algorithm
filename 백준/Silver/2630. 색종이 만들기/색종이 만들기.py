def cut_paper(x, y, n):
    global blue
    global white

    if n == 1:
        if papers[x][y] == 1: return 1
        else: return 0

    pieces = [0,0,0]
    n //= 2
    for i in a:
        p = cut_paper(x+(n*i[0]), y+n*(i[1]), n)
        pieces[p] += 1

    if pieces[0] == 4: return 0
    if pieces[1] == 4: return 1

    white += pieces[0]
    blue += pieces[1]
    return 2


N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
a = [[0,0], [0,1], [1,0], [1,1]]
blue = 0
white = 0
p = cut_paper(0,0, N)
if p == 0: white += 1
elif p == 1: blue += 1 
print(white)
print(blue)