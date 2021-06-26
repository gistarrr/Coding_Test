# 곱하기 혹은 더하기
numbers = input()

result = 0

if int(numbers[0]) <= 1 or int(numbers[1]) <= 1:
    result = int(numbers[0]) + int(numbers[1])
else :
    result = int(numbers[0]) * int(numbers[1])

for i in numbers[2:]:
    if int(i) <= 1 :
        result += int(i)
    else :
        result *= int(i)

print(result)