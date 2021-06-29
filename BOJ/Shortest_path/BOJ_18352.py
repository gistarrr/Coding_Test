from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
visited = [False] * (N+1)
flag = 1

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((X, 0))
distance[X] = 0
while q :
    node, dist = q.popleft()
    if not visited[node]:
        visited[node] = True
        for i in graph[node]:
            distance[i] = min(distance[i], dist + 1)
            q.append((i, distance[i]))
for i in range(1, N+1):
    if distance[i] == K:
        flag = 0
        print(i)
if flag :
    print(-1)