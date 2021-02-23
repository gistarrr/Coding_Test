import re

def solution1(new_id):
    answer = new_id.lower()
    exp = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in exp:
        answer = answer.replace(i,'')
    for i in range(5):
        answer = answer.replace('...','.').replace('..','.')
    if len(answer)>=1:
        if answer[0] == '.':
            answer = answer[1:]
    if answer == '':
        answer = 'a'
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]   
    if len(answer)<=2 :
        for i in range(len(answer)+1, 4):
            answer+=answer[-1]

    return answer

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub(r'[^a-z0-9\-_.]', '', st)
    st = re.sub(r'\.+', '.', st)
    st = re.sub(r'^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

ID = input()
print(solution2(ID))