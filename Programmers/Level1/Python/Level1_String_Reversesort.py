def solution(s):
    answer = ''

    for i in list(sorted(s, reverse = True)):
        answer += i
    return answer