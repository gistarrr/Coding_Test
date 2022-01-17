N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

#1 5 7 8 10 -> 1 5 10
houses.sort()

answer = 1
left = 1
right = houses[-1]-houses[0]

while left <= right :
    cnt = 1
    before = houses[0]
    distance = (left + right) // 2

    for i in range(1, len(houses)):
        if houses[i]-before >= distance:
            cnt += 1
            before = houses[i]

    if cnt >= C :
        left = distance + 1
        answer = distance
    else :
        right = distance - 1
print(answer)