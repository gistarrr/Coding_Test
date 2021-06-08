def solution(numbers, target):
    answer = 0
    
    def dfs(length, n_sum, target):
        nonlocal answer
        if length == 0:
            if n_sum == target:
                answer += 1
        else :
            dfs(length-1, n_sum + numbers[length-1], target)
            dfs(length-1, n_sum - numbers[length-1], target)
            
    dfs(len(numbers), 0, target)
    
    return answer