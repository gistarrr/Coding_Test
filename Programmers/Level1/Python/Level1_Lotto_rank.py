def solution(lottos, win_nums):
    answer = []

    Rank = 0

    ZeroCount = lottos.count(0)

    for i in win_nums:
        if i in lottos:
            Rank += 1

    min_rank = Rank
    max_rank = Rank + ZeroCount

    answer.append(rank_interchange(max_rank))
    answer.append(rank_interchange(min_rank))

    return answer

def rank_interchange(Rank):
    if Rank == 6:
        return 1
    elif Rank == 5:
        return 2
    elif Rank == 4:
        return 3
    elif Rank == 3:
        return 4
    elif Rank == 2:
        return 5
    else : 
        return 6

# Rank = [6, 6, 5, 4, 3, 2, 1]