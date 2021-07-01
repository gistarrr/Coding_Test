# 경쟁적 전염(백준 18405번)
from collections import deque
N, K = map(int, input().split())
graph = []
virus = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 :
            virus.append((graph[i][j], 0, i, j))
virus.sort()
q = deque(virus)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

S, X, Y = map(int, input().split())
while q:
    value, second, x, y = q.popleft()
    if second == S :
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = value
            q.append((value, second+1, nx, ny))

print(graph[X-1][Y-1])