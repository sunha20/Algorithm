a = int(input())
b = int(input())
c = int(input())

num = a*b*c
lst = [0]*10

while (num > 0):
    n = num % 10
    num //= 10
    lst[n] += 1

for i in lst:
    print(i)