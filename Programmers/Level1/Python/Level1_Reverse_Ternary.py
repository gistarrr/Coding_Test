# -*- coding: euc-kr -*-
def solution(n):
    answer = 0
    result = []
    while n > 0 :
        result.append(n%3)        
        n = n//3
    for i in range(len(result)):
        answer = answer + result[i]*3**(len(result)-1-i)

    return answer

#int(a, b) 형태