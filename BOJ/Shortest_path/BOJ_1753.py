import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start_node = int(input())
INF = int(1e9)
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
visited = [False] * (V+1)

for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

q = []
heapq.heappush(q, (0, start_node))
distance[start_node] = 0
while q :
    dist, now = heapq.heappop(q)
    if not visited[now] :
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        visited[now] = True

for i in range(1, V+1):
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])