def solution(numbers):
    answer = ''
    temp = list(map(lambda x : str(x)*4, numbers))
    result = sorted(temp, key = lambda x : (x[0], x[1], x[2], x[3]), reverse = True)
    for i in range(len(result)):
        result[i] = result[i][:len(result[i])//4]
        
    answer = "".join(result)
    if answer[0] == '0':
        return '0'
    else :
        return answer


# 가장 간단한 풀이
# temp = list(map(str, numbers))
# result = sorted(temp, key = lambda x : x*3, reverst = True)
# return str(int(''.join(result)))

# functools에서 cmp_to_key 함수를 이용하여 정렬 조건을 함수로 처리할 수 있다

