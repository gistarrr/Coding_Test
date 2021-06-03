from collections import deque

N, M, V = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]

graph = [ [] for _ in range(N+1) ]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for info in infos:
    graph[info[0]].append(info[1])
    graph[info[1]].append(info[0])

for i in range(N+1):
    graph[i].sort()

def dfs(graph, V, visited):
    visited[V] = True
    print(V, end=" ")
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, V, visited):
    queue = deque([V])
    visited[V] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)