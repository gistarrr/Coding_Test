N, M = map(int, input().split())
array = list(map(int, input().split()))

sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if array[i]+array[j]+array[k] <= M:
                sum = max(sum, array[i]+array[j]+array[k])
print(sum)