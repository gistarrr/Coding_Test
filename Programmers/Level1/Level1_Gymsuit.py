# -*- coding: euc-kr -*-
def solution(n, lost, reserve):
    answer = 0
    real_lost = []
    for i in lost:
        if i not in reserve:            
            real_lost.append(i)
        else :
            reserve.remove(i)
    
    for i in reserve:        
        for j in real_lost:
            if j == i-1 or j==i+1:
                real_lost.remove(j)
                break
        print(real_lost)
        
    
    answer = n - len(real_lost)          

    return answer

# def solution2(n, lost, reserve):
#     answer = 0

#     real_reserve = list(set(reserve)-set(lost))
#     real_lost = list(set(lost)-set(reserve))

#     #한 줄 for문 이용 가능

#     for i in real_reserve:
#         if i-1 in real_lost:
#             real_lost.remove(i-1)
#         elif i+1 in real_lost:
#             real_lost.remove(i+1)
    
#     answer = n - len(real_lost)

#     return answer

