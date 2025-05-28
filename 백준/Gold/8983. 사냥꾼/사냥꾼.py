def findUpper(n, arr):          # n = 동물의 x좌표
    S = 0                       # guns 좌표값에 대한 인덱스
    E = len(arr)
    while S < E:                    # upper bound 연산
        mid = (S + E) // 2
        if arr[mid] <= n:
            S = mid + 1
        else:
            E = mid
    else: return E

M, N, L = map(int, input().split())
guns = list(map(int, input().split()))
guns.sort()
cnt = 0
dicY = {}

for _ in range(N):
    x, y = map(int, input().split())    # 동물 위치

    # 해당 x에서 쏠 수 있는 거리(gunY) 구하기
    if x in dicY:
        gunY = dicY[x]
    else:
        e = findUpper(x, guns)  # 오른쪽에서 가까운 사대의 위치
        s = e - 1  # 왼쪽에서 가까운 사대의 위치

        diff = 0
        if s < 0:  # 주어진 x가 가장 작은 사대 위치보다도 작은 값일때,
            diff = guns[e] - x
        elif e >= len(guns):  # 주어진 x가 가장 큰 사대 위치보다도 큰 값일 때,
            diff = x - guns[s]
        else:
            diff = min(x - guns[s], guns[e] - x)
        gunY = L - diff
        dicY[x] = gunY

    if y <= gunY: cnt += 1
print(cnt)
