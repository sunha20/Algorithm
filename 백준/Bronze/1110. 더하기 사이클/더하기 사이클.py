N = int(input())
cnt = 1
num1 = N
num2 = N//10 + N%10
num = (num1 % 10)*10 + num2 % 10

while True:
    if num == N:
        break

    temp = num1 % 10 + num2 % 10
    num1 = num2
    num2 = temp
    num = (num1 % 10)*10 + num2 % 10
    cnt += 1

print(cnt)