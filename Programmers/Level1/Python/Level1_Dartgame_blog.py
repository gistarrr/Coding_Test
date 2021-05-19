def solution(dartResult):
    answer = 0
    
    Result = list(dartResult)
    Score = []
    
    for i in range(3):
        First_score = Result.pop(0)
        Secnd = Result.pop(0)

        if Secnd == '0':
            First_score += Secnd
            Secnd = Result.pop(0)
        First_score = int(First_score)

        if Secnd == 'D':
            First_score *= First_score
        elif Secnd == 'T':
            First_score = First_score*First_score*First_score
        try: 
            Third = Result[0]
            if Third == '*':
                Third = Result.pop(0)
                if len(Score) == 0:
                    First_score = First_score * 2
                    Score.append(First_score)
                else :
                    First_score *= 2
                    Score[-1] *= 2
                    Score.append(First_score)
            elif Third == '#':
                Third = Result.pop(0)
                First_score = -First_score
                Score.append(First_score)
            else :
                Score.append(First_score)

        except:
            Score.append(First_score)
            break
    
    for i in Score:
        answer += i

    return answer