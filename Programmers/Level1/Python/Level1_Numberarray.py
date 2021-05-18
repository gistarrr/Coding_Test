def solution(arr, divisor):
    answer = []

    for i in arr :
        if i % divisor == 0 :
            answer.append(i)
    answer.sort()
    if len(answer) < 1 :
        answer.append(-1)

    return answer

# def solution2(arr, divisor):
#     return sorted([n for n in arr if i % divisor == 0]) or [-1]