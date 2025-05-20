def hanoi(num, start, sub, dst):
    if num ==1:
        print(start, dst)
        return
    hanoi(num-1, start, dst, sub)       # (N-1)번째까지를 N번째 원판 위에서 치우기 -> 보조 막대로 옮기기
    print(start, dst)                   # N번째 원판을 목표 막대로 옮기기
    hanoi(num-1, sub, start, dst)       # (N-1)번째까지의 원판을 N번째 원판 위로 올리기 -> 보조막대에서 dst로.
    return

N = int(input())
print(2**N -1)
if (N <= 20):
    hanoi(N,1,2,3)