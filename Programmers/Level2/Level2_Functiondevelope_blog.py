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

# 모범답안 1
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]

#모범답안 2
# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

#모범답안 3
# from math import ceil

# def solution(progresses, speeds):
#     daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
#     count = 1
#     retList = []

#     for i in range(len(daysLeft)):
#         try:
#             if daysLeft[i] < daysLeft[i + 1]:
#                 retList.append(count)
#                 count = 1
#             else:
#                 daysLeft[i + 1] = daysLeft[i]
#                 count += 1
#         except IndexError:
#             retList.append(count)

#     return retList