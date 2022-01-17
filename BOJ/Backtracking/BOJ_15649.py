N, M = map(int, input().split())
visited = [False] * (N+1)
result = []
def dfs(count):
    global result
    if count == M:
        print(" ".join(map(str, result)))
        return
    else :
        for j in range(1, N+1):
            if not visited[j] :
                result.append(j)
                visited[j] = True
                dfs(count+1)
                result.pop()
                visited[j] = False
dfs(0)