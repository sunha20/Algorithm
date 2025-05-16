C = int(input())

for c in range(C):
    temp = list(map(int, input().split(" ")))
    N = temp[0]
    score = 0
    # 평균 구하기
    for n in range(1, N + 1):
        score += temp[n];

    avg = score / N
    up = 0
    # 학생 평가
    for n in range(1, N + 1):
        if temp[n] > avg:
            up += 1
    print(f"{((up / N) * 100):.3f}%")