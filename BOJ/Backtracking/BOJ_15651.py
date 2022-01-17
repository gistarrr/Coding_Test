N, M = map(int, input().split())
result = []
def dfs(count):
    global result
    if count == M:
        print(" ".join(map(str, result)))
        return
    else :
        for j in range(1, N+1):
            result.append(j)
            dfs(count+1)
            result.pop()
dfs(0)