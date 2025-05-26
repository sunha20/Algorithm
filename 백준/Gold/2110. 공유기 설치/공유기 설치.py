N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]
homes.sort()

dl = 1
dr = (homes[-1] - homes[0]) // (C-1) +1

while dl < dr:
    cnt = C - 1
    dm = (dr + dl) // 2

    # 설치
    i = 0
    for j in range(i, N):
        d = homes[j] - homes[i]
        if d >= dm:
            cnt -= 1
            i = j

    if cnt <= 0:        # 설치가 많이 되었으면
        dl = dm + 1     # 거리를 더 늘려야함
    else:               # 설치가 적게 되었으면
        dr = dm         # 거리를 줄여야함.

print(dr-1)