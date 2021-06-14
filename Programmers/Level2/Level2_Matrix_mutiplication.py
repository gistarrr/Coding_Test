def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            a=0
            for k in range(len(arr2)):
                a+=arr1[i][k]*arr2[k][j]
            answer[i].append(a)
    return answer

# 2차원 배열 뒤집기 => zip함수 * 이용