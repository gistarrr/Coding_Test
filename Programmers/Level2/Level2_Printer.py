def solution(priorities, location):
    answer = 0
    stack = []
    for i, v in enumerate(priorities):
        stack.append((i, v))
    print(stack)
    cnt = 0
    while stack:
        flag = 0
        index, important = stack.pop(0)
        for i in range(len(stack)):
            if  important < stack[i][1] :
                stack.append((index, important))
                flag = 1
                break
        if flag == 0:
            cnt += 1
            if index == location:
                break
    return cnt