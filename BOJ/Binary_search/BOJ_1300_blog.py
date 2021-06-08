import math

N = int(input())
k = int(input())

start = 0
end = k
answer = 0
while start <= end:
    mid = (start+end)//2
    tmp = 0
    # 갯수 구하기
    for i in range(1, N+1):
        tmp += min(N, mid // i)
    if tmp < k:
        start = mid + 1
    else :
        end = mid - 1
        answer = mid
print(answer)