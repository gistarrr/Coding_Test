def solution(record):
    answer = []
    
    id_dic = {}
    
    for String in record:
        result = String.split()
        if len(result) == 3:
            id_dic[result[1]] = result[2]
            
    for String in record:
        result = String.split()
        if result[0] == "Enter":
            answer.append(id_dic[result[1]]+"님이 들어왔습니다.")
        elif result[0] == "Leave":
            answer.append(id_dic[result[1]]+"님이 나갔습니다.")
            
    return answer