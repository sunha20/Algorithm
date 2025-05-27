def times(num, cnt, div):
    if cnt == 1:
        return num
    if cnt % 2 == 0:
        return (times(num, cnt//2, div)**2) % div
    else:
        return (times(num, cnt//2, div)**2 * num) % div

A,B,C = map(int, input().split())
A %= C
print(times(A, B, C))