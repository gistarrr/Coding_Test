from collections import deque

N, M, T = map(int, input().split())
castle = []
x_pos, y_pos = 0, 0
for i in range(N):
    castle.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if castle[i][j] == 2:
            x_pos, y_pos = i, j
            castle[i][j] = 0
special = [[0]*M for _ in range(N)]


def bfs(game_map, start_x, start_y, end_x, end_y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((start_x,start_y))
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<=end_x-1 and 0<=ny<=end_y-1 and game_map[nx][ny] == 0:
                game_map[nx][ny] = game_map[x][y] + 1
                q.append((nx, ny))
    return game_map[x_pos][y_pos], game_map[end_x-1][end_y-1]
a, b = bfs(castle, 0, 0, N, M)
if b == 0:
    if a == 0:
        result = 0
    else :
        result = a+bfs(special, x_pos, y_pos, N, M)[1]
else:
    if a == 0:
        result = b
    else :
        result = min(b, a+bfs(special, x_pos, y_pos, N, M)[1])

if result > T or result == 0 :
    print("Fail")
else :
    print(result)