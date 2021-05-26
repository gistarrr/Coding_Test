import math

Test_case = int(input())

result = []

for i in range(Test_case):
    H_W_N = list(map(int, input().split()))
    Room_H = str(H_W_N[2] % H_W_N[0])
    if Room_H == '0':
        Room_H = str(H_W_N[0])
    Room_W = str(math.ceil(H_W_N[2] / H_W_N[0]))
    if len(Room_W) == 1:
        Room_H += '0'
    result.append(Room_H+Room_W)

for i in result:
    print(i)