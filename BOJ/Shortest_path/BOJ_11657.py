import sys
input = sys.stdin.readline

INF = int(1e9)
Flag = False

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

distance = [INF] * (N+1)

distance[1] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in graph[j]:
            new_city = k[0]
            dist = k[1]
            if distance[j] != INF and distance[new_city] > distance[j] + dist :
                distance[new_city] = distance[j] + dist

    if i == N:
        for j in range(1, N+1):
            for k in graph[j]:
                new_city = k[0]
                dist = k[1]
                if distance[j] != INF and distance[new_city] > distance[j] + dist :
                    Flag = True

if Flag:
    print(-1)
else :
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else :
            print(distance[i])
    
