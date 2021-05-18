# -*- coding: euc-kr -*-
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        result = sorted(array[i-1:j])
        answer.append(result[k-1])
        
    return answer

# 한 줄 코드
# def solution2(array, commands):
#     return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))