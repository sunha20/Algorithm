def factorial_recursion(n):
    if (n == 0): return 1
    return factorial_recursion(n-1) * n

def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial_for(int(input())))
    # print(factorial_recursion(int(input())))