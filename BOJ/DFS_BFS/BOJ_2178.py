from collections import deque

N, M = map(int, input().split())

miro = []
for i in range(N):
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >=  M:
                continue
            elif miro[nx][ny] == 0:
                continue
            elif miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[N-1][M-1]

print(dfs(0, 0))


        