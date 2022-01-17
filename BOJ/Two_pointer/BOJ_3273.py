n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
answer = 0

numbers.sort()

left, right = 0, len(numbers)-1
while left<right :
    if numbers[left] + numbers[right] == x:
        answer += 1
        left += 1
        right -= 1
    elif numbers[left] + numbers[right] < x :
        left += 1
    else :
        right -= 1
print(answer)