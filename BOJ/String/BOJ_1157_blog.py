import collections

S = input()
S = S.upper()
answer = collections.Counter(S)
if len(S) >1:
    if answer.most_common(2)[0][1] == answer.most_common(2)[1][1]:
        print('?')
    else :
        print(answer.most_common(2)[0][0])
else :
    print(S)