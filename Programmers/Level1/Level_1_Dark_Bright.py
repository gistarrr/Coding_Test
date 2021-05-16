def solution(absolutes, signs):
    answer = 0
    
    for i,j in enumerate(absolutes):
        if signs[i] == False:
            j = -j
        answer += j
        
    return answer