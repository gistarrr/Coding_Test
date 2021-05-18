def solution(N, stages):
    answer = []

    user_dict = {}
    user_num = len(stages)

    stages.sort()

    for i in range(1, N+1):
        try:
            fail_rate = stages.count(i) / user_num
            user_dict[i] = fail_rate
        except:
            user_dict[i] = 0
        user_num -= stages.count(i)
    user_dict = sorted(user_dict.items(), key = lambda x : x[1], reverse = True)

    for i in user_dict:
        answer.append(i[0])

    # answer = sorted(user_dict, key = lambda x : user_dict[x], reverse = True)

    return answer