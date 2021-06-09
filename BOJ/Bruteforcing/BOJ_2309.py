from itertools import combinations

array = []
for i in range(9):
    array.append(int(input()))

result = list(combinations(array, 7))
for i in result:
    if sum(i) == 100:
        answer = list(i)
answer.sort()

for i in range(7):
    print(answer[i])