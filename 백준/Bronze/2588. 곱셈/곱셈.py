A = int(input())
B = int(input())
b = B

while (b != 0):
    c = b % 10
    b //= 10
    
    print(A * c)
    
print(A*B)