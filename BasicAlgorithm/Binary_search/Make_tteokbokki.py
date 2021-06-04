N, M = map(int, input().split())

height = list(map(int, input().split()))

start = 0
end = max(height)

while start<=end:
    result = 0
    mid = (start + end) // 2    
    # print(start, mid, end)
    for i in height:
        if i > mid:
            result += i - mid
    # print(result)
    if result == M:
        print(mid)
        break

    elif result > M:
        start = mid+1

    else :
        end = mid - 1




