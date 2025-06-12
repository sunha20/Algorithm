n = int(input())
cnt = [0,0] # 2, 5
for coin in [5,2]:
    cnt[coin%2] += n//coin
    n %= coin

if n == 1:
    if cnt[5%2] == 0:
        print(-1)
    else:
        print(sum(cnt) + 2)

else:
    print(sum(cnt))