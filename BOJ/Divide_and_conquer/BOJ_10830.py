N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
odd = A
def calculate_matrix(matrixA, matrixB):
    cal_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += matrixA[i][k] * matrixB[k][j]
            cal_matrix[i][j] = temp % 1000
    return cal_matrix

cal_list = []

while B > 1 :
    if B % 2 == 0:
        B = B//2
        cal_list.append(False)
    else :
        B = B//2
        cal_list.append(True)

for i in range(len(cal_list)-1, -1, -1):
    if cal_list[i]:
        A = calculate_matrix(calculate_matrix(A, A), odd)
    else :
        A = calculate_matrix(A, A)

for i in range(N):
    for j in range(N):
        print(A[i][j] % 1000, end = ' ')
    print()