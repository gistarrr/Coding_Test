from itertools import permutations

def solution(numbers):
    answer = 0
    real = set()
    choice = list(numbers)
    for i in range(1, len(numbers)+1):
        result = list(map(int, list(map("".join, permutations(choice, i)))))
        real = set(result) | real
    for i in real:
        if is_prime(i) == True:
            answer += 1
    return answer

def is_prime(number):
    if number == 0 or number ==1 :
        return False
    else :
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True