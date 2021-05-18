# -*- coding: euc-kr -*-
def solution(answers):
    answer = []
    P_1 = [1, 2, 3, 4, 5]
    P_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    P_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {1 : 0, 2 : 0, 3 : 0}
    for i in range(len(answers)):
        if P_1[i%5] == answers[i]:
            count[1]+=1
        if P_2[i%8] == answers[i]:
            count[2]+=1
        if P_3[i%10] == answers[i]:
            count[3]+=1

    count = sorted(count.items(), key=lambda x : x[1], reverse=True)
    answer.append(count[0][0])

    if count[0][1] == count[1][1]:
        answer.append(count[1][0])
        if count[1][1] == count[2][1]:
            answer.append(count[2][0])    
    return answer

# enumerate 함수 이용
# 리스트 내포 응용
# itertools 모듈에 있는 cycle

def soultion2(answers):
    Pattern = [[1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    Score = [0]*len(Pattern)

    for num, pro in enumerate(answers):
        for idx, pat in enumerate(Pattern):
            if pro == pat[num%len(pat)]:
                Score[idx] += 1
    return [i+1 for i, v in enumerate(Score) if v==max(Score)]