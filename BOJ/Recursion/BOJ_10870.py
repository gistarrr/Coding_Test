def fibonacci(N : int):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else :
        return fibonacci(N-1) + fibonacci(N-2)

N = int(input())
print(fibonacci(N))