def solution(prices):
    answer = [0]*len(prices)

    stack = []

    for i, v in enumerate(prices):
        if stack:
            while stack and stack[-1][1] > v :
                index, time = stack.pop()
                answer[index] = i - index 
            stack.append((i, v))
        else:
            stack.append((i, v))            
    while stack:
        index, time = stack.pop()
        answer[index] = len(prices) - index - 1

    return answer