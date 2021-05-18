def solution(d, budget):
    answer = 0

    d.sort()

    for i in d:
        budget -= int(i)
        if budget<0:
            break
        else:            
            answer+=1    
    return answer