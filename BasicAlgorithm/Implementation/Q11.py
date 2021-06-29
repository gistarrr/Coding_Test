# 뱀 (백준 3190번)

from collections import deque
N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

x = [0, 1, 0, -1]
y = [1, 0, -1, 0]

snake_pos = []
snake_rotate = deque()
L = int(input())
for i in range(L):
    a, b = input().split()
    snake_rotate.append((int(a), b))

def check_direction(snake_rotate, time, index):
    if snake_rotate and snake_rotate[0][0] == time :
        if snake_rotate[0][1] == 'D':
            index += 1
        else :
            index -= 1
        snake_rotate.popleft()
    if index <= -1 :
        index = 3
    elif index >= 4 :
        index = 0
    return index
time = 0
i = 0
snake_pos.append((0, 0))
x_pos = 0
y_pos = 0
board[0][0] = 2
while True :
    i = check_direction(snake_rotate, time, i)
    time += 1
    if x_pos+x[i] < 0 or x_pos+x[i] >= N or y_pos+y[i] < 0 or y_pos+y[i] >= N:
        break
    if board[x_pos+x[i]][y_pos+y[i]] == 2:
        break
    if board[x_pos+x[i]][y_pos+y[i]] == 1:
        board[x_pos+x[i]][y_pos+y[i]] = 2
        x_pos = x_pos+x[i]
        y_pos = y_pos+y[i]
        snake_pos.append((x_pos, y_pos))
    else :
        board[x_pos+x[i]][y_pos+y[i]] = 2
        x_pos = x_pos+x[i]
        y_pos = y_pos+y[i]
        snake_pos.append((x_pos, y_pos))
        dx, dy = snake_pos.pop(0)
        board[dx][dy] = 0
print(time)