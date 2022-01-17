from collections import Counter
import math
import sys
input = sys.stdin.readline

n = int(input())
sum_value = 0
num_dict = {}
numbers = []
for i in range(n):
    a = int(input())
    numbers.append(a)
    sum_value += a
    if a in num_dict.keys():
        num_dict[a] += 1
    else :
        num_dict[a] = 1
numbers.sort()
num_dict = sorted(num_dict.items(), key = lambda x : (x[1], -x[0]))
print(round(sum_value/len(numbers)))
print(numbers[len(numbers)//2])

if len(num_dict)>1 and num_dict[-1][1] == num_dict[-2][1]:
    print(num_dict[-2][0])
else :
    print(num_dict[-1][0])
print(numbers[-1]-numbers[0])