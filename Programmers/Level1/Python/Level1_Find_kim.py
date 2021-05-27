def solution(seoul):
    answer = ''
    
    for index, value in enumerate(seoul):
        if value == "Kim":
            answer = f'김서방은 {index}에 있다'
    return answer

# seoul.index("Kim")