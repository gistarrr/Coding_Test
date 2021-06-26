# 문자열 재정렬
S = input()
alpha = []
number = []
for i in S:
    if i.isalpha():
        alpha.append(i)
    else:
        number.append(i)
alpha.sort()
sum_num = sum(map(int, number))
result = "".join(alpha) + str(sum_num)
print(result)