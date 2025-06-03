import sys
input = __import__('sys').stdin.readline

def dfs(i, val):
    if i == N-1:
        resultList.append(val)
        return

    if operators['+'] > 0:
        operators['+'] -= 1
        dfs(i+1, val + lst[i+1])
        operators['+'] += 1

    if operators['-'] > 0:
        operators['-'] -= 1
        dfs(i+1, val - lst[i+1])
        operators['-'] += 1

    if operators['*'] > 0:
        operators['*'] -= 1
        dfs(i+1, val * lst[i+1])
        operators['*'] += 1

    if operators['//'] > 0:
        operators['//'] -= 1
        if val < 0:
            dfs(i+1, -(-val // lst[i+1]))
        else:
            dfs(i+1, val // lst[i+1])
        operators['//'] += 1


N = int(input())
lst = list(map(int, input().split()))
temp = list(map(int, input().split()))
operators = {'+': temp[0], '-': temp[1], '*': temp[2], '//': temp[3]}
resultList = []
dfs(0, lst[0])
resultList.sort()

print(resultList[-1])
print(resultList[0])