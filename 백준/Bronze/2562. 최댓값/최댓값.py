maxNum = 0
idx = -1
for i in range(1,10):
    now = int(input())
    if maxNum < now:
        maxNum = now
        idx = i
    
print(maxNum)
print(idx)