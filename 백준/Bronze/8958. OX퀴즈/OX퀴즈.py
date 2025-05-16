T = int(input())
for _ in range(T):
    ox = input()
    score = 0
    cnt = 0
    for i in ox:
        if i == "O":
            cnt += 1
            score += cnt
            
        else:
            cnt = 0;
    print(score)
        