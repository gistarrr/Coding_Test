N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
visited = [False]*(len(array))
result = []
def dfs(count):
    if count == M:
        print(" ".join(map(str, result)))
        return
    else :
        for i in range(len(array)):
            if not visited[i] :
                result.append(array[i])
                visited[i] = True
                dfs(count+1)
                result.pop()
                visited[i] = False
dfs(0)