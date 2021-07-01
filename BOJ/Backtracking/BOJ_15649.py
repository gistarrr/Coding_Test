N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = []
def dfs(i, count):
    global result
    if count == M:
        print(result)
        result = result[:-1]
        return
    else :
        for j in range(i+1, N):
            result.append(numbers[i])
            dfs(j, count+1)
            result = result[:-1]

dfs(0, 0)

