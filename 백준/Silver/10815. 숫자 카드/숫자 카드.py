N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))

for m in range(M):
    lo = 0
    hi = N-1
    num = nums[m]
    while lo <= hi:
        mid = (lo+hi)//2
        card = cards[mid]
        if card == num:
            print(1, end=" ")
            break
        elif card < num:
            lo = mid + 1
        else:
            hi = mid - 1
    else:
        print(0, end=" ")