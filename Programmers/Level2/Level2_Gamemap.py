from collections import deque 

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >=N or ny >= M:
                continue
            elif maps[nx][ny] == 0:
                continue
            elif maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    if maps[N-1][M-1] != 1:
        return maps[N-1][M-1]
    else :
        return -1