N, M = map(int, input().split())
visited = [0] * (N+1)
result = []
def dfs(count, start):
    if count == M:
        print(" ".join(map(str, result)))
        return
    else :
        for i in range(start, N+1):
            if not visited[i] :
                result.append(i)
                visited[i] = True
                dfs(count+1, i+1)
                result.pop()
                visited[i] = False
dfs(0, 1)