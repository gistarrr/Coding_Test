# 1st try
# def solution(progresses, speeds):
#     answer = []
    
#     progress_date = []
    
#     for progress, speed in zip(progresses, speeds):
#         complete_date = 0
#         while(progress <100):
#             progress+=speed
#             complete_date += 1
#         progress_date.append(complete_date)
    
#     i = 0
    
#     while(i < len(progress_date)):
#         count = 1
#         i += 1
#         while(i < len(progress_date)):
#             if(progress_date[i-1] >= progress_date[i]):
#                 count+=1
#                 i += 1
#             else:
#                 break
#         answer.append(count)
            
#     return answer
# test case = [97. 98, 97] [1, 1, 1] -> 3일 2일 3일 -> 출력 : 3

def solution(progresses, speeds):
    answer = []

    progress_date = []

    for progress, speed in zip(progresses, speeds):
        complete_date = 0
        while(progress <100):
            progress+=speed
            complete_date += 1
        progress_date.append(complete_date)

    i = 0

    while(i < len(progress_date)):
        count = 1
        i += 1
        j = i
        while(j < len(progress_date)):
            if(progress_date[i-1] >= progress_date[j]):
                count+=1
                j += 1
            else:
                break
        i = j
        answer.append(count)

    return answer