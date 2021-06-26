# 문자열 뒤집기
S = input()
first = S[0]
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] != first:
            count += 1
print(count)
