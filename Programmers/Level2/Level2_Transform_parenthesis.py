answer = ''

def solution(p):
    
    answer = seperate(p)
    return answer

def check(p):
    stack = []
    if len(p) == 0:
        return True
    stack.append(p[0])
    for i in p[1:]:
        if stack and stack[-1] == '(' and i == ')':
            stack.pop()
        else :
            stack.append(i)
    if stack:
        return False
    else :
        return True
    
def reverse(u):
    rev = ''
    if len(u) != 0: 
        for i in range(len(u)):
            if u[i] == '(':
                rev += ')'
            elif u[i] == ')':
                rev += '('
    return rev
    
def seperate(p):
    a_cnt, b_cnt = 0, 0
    u, v = '', ''
    if len(p) == 0:
        return p
    else:
        for i in range(len(p)):
            u += p[i]
            if p[i] == '(':
                a_cnt +=1
            elif p[i] == ')':
                b_cnt +=1
            if a_cnt == b_cnt:
                if i+1 <= len(p)-1:
                    v += p[i+1:]
                break
    print(u)
    if check(u) and check(v):
        answer = u+v
        return answer
    elif check(u) and check(v) == False :
        answer = u + seperate(v)
        return answer
    elif check(u) == False:
        temp = '(' + seperate(v) + ')'
        u = reverse(u[1:-1])
        answer = temp + u
        return answer

# 다른 풀이

# def solution(p):
#     if p=='': return p
#     r=True; c=0
#     for i in range(len(p)):
#         if p[i]=='(': c-=1
#         else: c+=1
#         if c>0: r=False
#         if c==0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))