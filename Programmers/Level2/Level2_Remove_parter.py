def solution(s):
    answer = 0

    stack = []
    stack.append(s[0])
    for char in s[1:]:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        answer = 1        

    return answer