# 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))

target = 1
for x in data:
    if target < x:
        break
    target += 1

print(target)