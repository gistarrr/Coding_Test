import heapq
import sys
input = sys.stdin.readline


INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
V_1, V_2 = map(int, input().split())

def dijkstra(start_node, end_node):
    distance = [INF]*(N+1)
    visited = [False]*(N+1)
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)
        if not visited[node]:
            for i in graph[node]:
                cost = i[1] + dist
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
            visited[node] = True
    
    return distance
dist = INF

first = dijkstra(V_1, V_2)
second = dijkstra(V_2, V_1)
dist = min(dist, first[1] + first[V_2] + second[N], first[N] + second[V_1] + second[1])

print(-1) if dist >= INF else print(dist)
