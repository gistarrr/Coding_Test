import math

T = int(input())

for i in range(T):
    x, y = map(int, input().split())

    N = int(math.sqrt(y-x))

    if N ** 2 == y - x :
        print(2*N-1)
    elif  N ** 2 < y-x < N ** 2 + N :
        print(2*N)
    else :
        print(2*N+1)
     