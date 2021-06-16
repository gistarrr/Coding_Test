INF = int(1e9)
import heapq
N, M, C = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF]*(N+1)
visited = [False]*(N+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, distance[start]))
    while q:
        now, dist = heapq.heappop(q)
        visited[now] = True
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

dijkstra(C)
max_value = 0
count = 0
for i in range(1, len(distance)):
    if max_value < distance[i] and distance[i] < INF :
        max_value = distance[i]
    if 0 < distance[i] < INF :
        count += 1

print(count, max_value)
