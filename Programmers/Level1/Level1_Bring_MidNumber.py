# -*- coding: euc-kr -*-
def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2-1]+s[len(s)//2]
    return answer

# 한 줄 풀이
# def solution1(s):
#     return s[(len(s)-1)//2:len(s)//2+1]