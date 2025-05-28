from collections import deque

p = input()
stk = deque()
closes = {'(': (')', 2), '[': (']', 3)}

for i in range(len(p)):

    if p[i] in closes:
        stk.append(p[i])
        continue

    # pop을 해야함
    add = 0
    while True:
        if len(stk) == 0:
            print(0)
            exit()

        if type(stk[-1]) is int:
            add += stk.pop()
            continue

        c = closes[stk[-1]][0]
        score = closes[stk[-1]][1]
        if p[i] == c:        # 제대로 닫힘
            stk.pop()
            stk.append(max(score, score * add))
            break
        else:
            print(0)
            exit()
try:
    print(sum(stk))
except:
    print(0)
