N = int(input())
S = list(map(int, input().split()))

S.sort()

min_value, max_value = -2000000000,2000000000

answer = None
l_answer = None
r_answer = None
left, right = 0, len(S)-1

while left<right:
    if S[left] + S[right] == 0:
        answer = (left, right)
        break
    elif S[left] + S[right] < 0:
        if S[left] + S[right] > min_value :
            l_answer = (left, right)
            min_value = S[left] + S[right]
        left += 1
    elif S[left] + S[right] > 0:
        if S[left] + S[right] < max_value:
            r_answer = (left, right)
            max_value = S[left] + S[right]
        right -= 1
if answer is not None:
    print(S[answer[0]], S[answer[1]])
elif r_answer is None and l_answer is not None:
    print(S[l_answer[0]], S[l_answer[1]])
elif l_answer is None and r_answer is not None:
    print(S[r_answer[0]], S[r_answer[1]])
else :
    if abs(S[l_answer[0]] + S[l_answer[1]]) < S[r_answer[0]] + S[r_answer[1]]:
        print(S[l_answer[0]], S[l_answer[1]])
    else :
        print(S[r_answer[0]], S[r_answer[1]])