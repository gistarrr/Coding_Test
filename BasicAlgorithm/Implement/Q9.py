# 문자열 압축
def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2 + 1):
        compressed = ''
        cnt = 1 
        prev = s[:step]
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else :
                compressed += str(cnt) + prev if cnt > 1 else prev
                prev = s[j:j+step]
                cnt = 1
        answer = min(answer, len(compressed))
    return answer