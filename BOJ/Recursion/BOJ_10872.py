def fact(N : int):
    if N <= 1:
        return 1
    else :
        return N * fact(N-1)

N = int(input())

print(fact(N))