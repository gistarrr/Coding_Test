import re

def solution(files):
    sort_Ex = []
    answer=[]
    for file in files:
        HEAD = re.match(r'[a-zA-Z\s.-]+',file).group()
        NUMBER = re.search(r'[\d]+',file).group()
        idx = re.search(r'[\d]+',file).end()
        TAIL = file[idx:]
        if len(NUMBER) >= 6:
            TAIL = NUMBER[5:]+TAIL
            NUMBER = NUMBER[:5]            
        result = {'HEAD':HEAD, 'NUMBER': NUMBER,'TAIL':TAIL}
        sort_Ex.append(result)

    sort_results = sorted(sort_Ex, key= lambda x : (x['HEAD'].lower(), int(x['NUMBER'])))

    for sort_result in sort_results:
        name = sort_result['HEAD']+sort_result['NUMBER']+sort_result['TAIL']
        answer.append(name)
    
    return answer