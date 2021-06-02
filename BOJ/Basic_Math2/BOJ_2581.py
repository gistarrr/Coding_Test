M = int(input())
N = int(input())

total_sum = 0
min_num = N

for number in range(M, N+1):
    flag = True
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            flag = False
    if flag and number != 1 :
        total_sum += number
        min_num = min(min_num, number)

if total_sum == 0:
    print("-1")
else:  
    print(f'{total_sum}\n{min_num}') 

        