N, M = map(int, input().split())
result = []
def dfs(count, start):
    global result
    if count == M:
        print(" ".join(map(str, result)))
        return
    else :
        for j in range(start, N+1):
            result.append(j)
            dfs(count+1, j)
            result.pop()
dfs(0, 1)