def solution(arr):
    a=[]
    a.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]: continue
        else : a.append(arr[i])
    return a

# def no_continuous(s):
#    a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a