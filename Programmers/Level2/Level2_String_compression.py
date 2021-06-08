def solution(s):
    answer = len(s)
    
    length = len(s)//2
    
    
    for i in range(1, length + 1):
        result = []
        index = 0
        number = 1
        while index+2*i <= len(s)+i:
            if s[index:index + i] == s[index + i:index + 2*i]:
                index += i
                number += 1
            else :
                if number != 1:
                    result.append(str(number))
                    result.append(s[index:index + i])
                    index += i
                    number = 1
                else :
                    result.append(s[index:index + i])
                    index += i
        result.append(s[index:index + i])
        zip_stirng = "".join(result)
        answer = min(answer, len(zip_stirng))
        
    return answer