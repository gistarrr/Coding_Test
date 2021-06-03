from collections import deque

T = int(input())

def bfs(x, y, end_x, end_y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    while queue :
        x, y = queue.popleft()

        for i in range(len(knight)):
            nx = x + knight[i][0]
            ny = y + knight[i][1]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            elif visited[nx][ny] != 0:
                continue
            else :
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
        if x == end_x and y == end_y:
            return visited[x][y]

for _ in range(T):
    N = int(input())
    cur_pos_x, cur_pos_y  = map(int, input().split())
    fu_pos_x, fy_pos_y = map(int, input().split())

    visited = [[0]*N for _ in range(N)]

    knight = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

    print(bfs(cur_pos_x, cur_pos_y, fu_pos_x, fy_pos_y))