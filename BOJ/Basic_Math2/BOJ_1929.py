from sys import stdin
M, N = map(int, stdin.readline().split())

array = [True] * (N+1)
array[0] = False
array[1] = False

for i in range(2, int(N**0.5)+1):
    if array[i]:
        for j in range(2, N // i + 1):
            array[i*j] = False

for number in range(M, N+1):
    if array[number]:
        print(number)