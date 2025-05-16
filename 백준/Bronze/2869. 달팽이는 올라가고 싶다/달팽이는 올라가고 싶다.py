import math

A, B, V = map(int, input().split())

V -= A  # 끝에 도달했는지 검증하는 시기가 올라간 직후니까. 이걸 해주지 않으면 내려간 후에 검증을 하게됨. 대신 이후에 하루 더해줘야함.

q = math.ceil(V/(A-B)) # 내려갔다 올라갔다를 며칠씩 하는지.

print(q + 1)