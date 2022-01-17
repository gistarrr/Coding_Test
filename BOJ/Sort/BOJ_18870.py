N = int(input())
numbers = list(map(int, input().split()))\

check = sorted(list(set(numbers)), reverse=True)

check_dict = {}

for i, v in enumerate(check):
    check_dict[v] = i

result = []
for i in numbers :
    result.append(len(check_dict)-1-check_dict[i])
print(' '.join(map(str, result)))