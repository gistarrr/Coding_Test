T = int(input())

Number = list(map(int, input().split()))

count = 0

for i in Number:
    Prime_flag = True
    if i == 1:
        Prime_flag = False
    elif i == 2:
        Prime_flag = True
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                Prime_flag = False
                break
    if Prime_flag:
        count+=1
print(count)