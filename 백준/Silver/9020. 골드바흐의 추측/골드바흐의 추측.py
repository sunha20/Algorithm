T = int(input())
targets = []
for _ in range(T):
    targets.append(int(input()))

primes = [0]*(max(targets)+1)

for i in range(2, len(primes)):
    if (i == 1): continue   # 이미 채워졌으면 넘어감 -> 자기 자신의 배수도 이미 다 지워졌기 때문에.

    for check in range(i+1, len(primes)):
        if check % i == 0:
            primes[check] = 1

for t in targets:
    for i in range(t//2, t):
        if primes[i] == 1:
            continue

        if primes[t-i] == 0:
            print(f"{t-i} {i}")
            break