import re
def solution(s):
    answer = ''
    
    p = re.compile("( *\w+ *)")
    result = re.findall(p, s)
    
    for i in result:
        index = 0
        while i[index] == " ":
            index += 1
        if i[index].isalpha():
            k = i[0:index] + i[index].upper() + i[index+1:].lower()
        else :
            k = i.lower()
        answer += k

    return answer