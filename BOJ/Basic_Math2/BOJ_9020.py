import math

T = int(input())

def prime(N : int):
    total_prime = [False, False] + [True]*(N-1)
    for i in range(2, int(math.sqrt(N))+1):
        for j in range(2, N//i+1):
            total_prime[i*j] = False
    return total_prime

for i in range(T):
    N = int(input())
    result = []

    prime_list = prime(N)

    for i in range(len(prime_list)):
        if prime_list[i] == True:
            if prime_list[N-i] == True:
                prime_list[i] = False
                prime_list[N-i] = False
                result.append((i, N-i))

    print(result[-1][0], result[-1][1])