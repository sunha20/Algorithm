N = int(input())

if N < 100:
    print(N)
else:
    if N == 1000: N -= 1

    sum = 99
    numList = [0,0,0]

    for num in range(100, N+1):
        for i in range(3):
            numList[i] = num%10
            num //= 10

        if numList[0] - numList[1] == numList[1] - numList[2]:
            sum += 1

    print(sum)