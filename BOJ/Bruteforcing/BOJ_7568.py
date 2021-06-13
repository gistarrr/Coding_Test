N = int(input())

array = [list(map(int, input().split())) for i in range(N)]

result = []

for i in range(len(array)):
    cnt = 0
    for j in range(len(array)):
        if i == j :
            continue
        if array[j][0] > array[i][0] and array[j][1] > array[i][1]:
            cnt += 1
    result.append(cnt+1)
for i in result:
    print(i, end = ' ')

# 문제를 꼼꼼하게 읽고 풀 것 !!!