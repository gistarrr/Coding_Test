from collections import Counter
def solution(str1, str2):
    answer = 0
    a = []
    b = []
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        for i in temp:
            if not i.isalpha():
                break
        else:
            a.append(temp.lower())
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        for i in temp:
            if not i.isalpha():
                break
        else:
            b.append(temp.lower())

    hap = dict(Counter(a))
    cha = {}
    for key, item in Counter(b).items():
        if key in hap.keys() :
            hap[key] = max(hap[key], item)
        else :
            hap[key] = item
    for key, item in Counter(b).items():
        if key in Counter(a).keys():
            cha[key] = min(Counter(a)[key], item)
    print(hap, cha)
    A, B = 0, 0
    for i in hap.values():
        A += i
    for i in cha.values():
        B += i
    if A == 0:
        answer = 65536
    else:
        answer = int(B/A*65536)

    return answer