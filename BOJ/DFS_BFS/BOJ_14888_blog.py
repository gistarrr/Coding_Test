# 연산자 끼워넣기 (백준 14888번)
from itertools import permutations
N = int(input())
numbers = list(map(int,input().split()))
op_num = list(map(int, input().split()))
op_list = ''
for i in range(4):
    if i == 0:
        op_list += '+'*op_num[i]
    elif i == 1:
        op_list += '-'*op_num[i]
    elif i == 2:
        op_list += '*'*op_num[i]
    elif i == 3:
        op_list += '/'*op_num[i]
op_list = set(permutations(list(op_list), len(op_list)))
max_value = -1000000001
min_value = 1000000001
for i in op_list:
    result = numbers[0]
    for j in range(0, len(i)):
        if i[j] == '+':
            result += numbers[j+1]
        elif i[j] == '-':
            result -= numbers[j+1]
        elif i[j] == '*':
            result *= numbers[j+1]
        elif i[j] == '/':
            if result < 0:
                result = -result
                result //= numbers[j+1]
                result = -result
            else :
                result //= numbers[j+1]
    if result > max_value :
        max_value = result
    if result < min_value :
        min_value = result
print(max_value)
print(min_value)