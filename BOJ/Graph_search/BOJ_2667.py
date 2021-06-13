dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
house = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

result = []
check = 0
cnt = 0
def dfs(x, y):
    global cnt
    if house[x][y] == 0:
        return False
    else :
        cnt += 1
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
        return True

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt = 0
            if dfs(i, j):
                check += 1
                result.append(cnt)
result.sort()
print(check)
for i in result:
    print(i)