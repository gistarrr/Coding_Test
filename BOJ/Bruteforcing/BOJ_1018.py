N, M = map(int, input().split())
chess = []
answer1 = 0
answer2 = 0
for i in range(N):
    chess.append(list(input()))
check = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
min_value = 64
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        index1 = 0
        index2 = 1
        for k in range(8):
            for l in range(8):
                if chess[i+k][j+l] != check[index1][l]:
                    answer1 += 1
                if chess[i+k][j+l] != check[index2][l]:
                    answer2 += 1
            index1 = (index1+1)%2
            index2 = (index2+1)%2
        min_value = min(min_value, answer1, answer2)
        answer1 = 0
        answer2 = 0
print(min_value)