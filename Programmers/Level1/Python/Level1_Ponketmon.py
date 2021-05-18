def solution(nums):
    answer = 0

    new_nums = list(set(nums))

    if len(new_nums) < len(nums) / 2 :
        answer = len(new_nums)
    else :
        answer = len(nums) / 2

    return answer