N = int(input())
lst = [N//10, N%10, N//10 + N%10]

i = 1
num = 0
while True:
    a = lst[i] % 10
    b = lst[i+1] % 10
    num = a*10 + b

    lst.append(a+b)
    if (num == N):
        break
    i+=1

print(len(lst)-3)