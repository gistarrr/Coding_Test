import re
def oper(numbers, operation, index):
    if operation == '*':
        a, b = numbers.pop(index), numbers.pop(index)
        numbers.insert(index, a*b)
    elif operation == '+':
        a, b = numbers.pop(index), numbers.pop(index)
        numbers.insert(index, a+b)
    elif operation == '-':
        a, b = numbers.pop(index), numbers.pop(index)
        numbers.insert(index, a-b)

def solution(expression):
    answer = 0
    result = []
    numbers = list(map(int, re.findall('\d+', expression)))
    operations = re.findall('\D', expression)
    seq = ['*+-', '*-+','+-*','+*-','-*+','-+*']
    for i in range(6):
        temp = numbers[:]
        temp_oper = operations[:]
        for j in range(3):
            cnt = 0
            for k in range(0, len(temp_oper)):
                index = k - cnt
                if temp_oper[index] == seq[i][j]:
                    oper(temp, temp_oper[index], index)
                    temp_oper.pop(index)
                    cnt += 1
        result.append(temp[0])
    for i in range(len(result)):
        result[i] = abs(result[i])
    answer = max(result)    
    return answer