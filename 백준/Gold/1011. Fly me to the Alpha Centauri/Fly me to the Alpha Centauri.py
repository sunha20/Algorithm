'''
양 옆에서 오면 좋을 것 같은데.
그지. 반절만 하자. 해서 2배를 하면 되잖아.
그러면
1. 중간에 딱 도달하거나
2. 중간의 중간에 딱 도달하거나

아니야 일단 한번 써보자

1-5

2: 1
4: 12
5: 121

거리별
1: 1 ** 1 11 -> 1
2: 11
3: 111
4: 121 ** 2 22 -> 3
5: 1211
6: 1221
7: 12211
8: 12221
9: 12321 ** 3 33 -> 5
10: 123211
11: 123221
12: 123321
13: 1233211
14: 1233221
15: 1233321
16: 1234321 ** 4 44 -> 7

'''

import sys, math

def spaceship():
    N = int(sys.stdin.readline().rstrip())

    while N > 0:
        # setting
        N -= 1
        now, end = map(int, sys.stdin.readline().split())
        distance = end - now

        # calculate
        flag = math.sqrt(distance)

        if (flag % 1 == 0):
            print(int(flag) * 2 - 1)
        elif (0 < flag%1 < 0.5):
            print(int(flag) * 2)
        else:
            print(int(flag) * 2 + 1)
        # result


if __name__ == "__main__":
    spaceship()

