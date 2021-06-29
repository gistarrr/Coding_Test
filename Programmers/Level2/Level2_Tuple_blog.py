def solution(s):
    answer = []
    n_tuple = s[1:-1]
    result = []
    temp = []
    num = ''
    for i in range(len(n_tuple)):
        if  n_tuple[i].isdigit():
            num += n_tuple[i]            
        elif n_tuple[i-1] != '}' and n_tuple[i] == ',':
            temp.append(int(num))
            num = ''
        elif n_tuple[i] == '}':
            temp.append(int(num))
            result.append(temp[:])
            num = ''
            temp.clear()
    result.sort(key = lambda x : len(x))
    answer += result[0]
    for i in range(0, len(result)-1):
        answer += list(set(result[i+1])-set(result[i]))   
    
    return answer