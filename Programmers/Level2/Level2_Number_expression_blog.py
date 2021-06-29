def solution(n):
    answer = 0
    for i in range(1, (n+1)//2 + 1):
        sum = i
        for j in range(i+1, (n+1)//2 + 2):
            sum += j
            if sum == n:
                answer += 1
                break
            if sum > n :
                break
    answer += 1
            
    return answer