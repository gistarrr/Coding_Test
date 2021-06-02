import math

def is_prime(N : int)-> int:
    
    cnt = 0
    array = [False, False] + [True]*(2*N-1)

    for index in range(2, int(math.sqrt(2*N))+1):
        if array[index]:
            for j in range(2,(2*N//index)+1):
                array[index*j] = False
    
    for i in range(N+1, 2*N +1):
        if array[i]:
            cnt+=1
    return cnt

while True:
    N = int(input())
    if N == 0:
        break
    print(is_prime(N))
