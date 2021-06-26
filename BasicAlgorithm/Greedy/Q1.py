# 모험가 길드
N = int(input())
members = list(map(int, input().split()))
members.sort()

result = 0
count = 0

for i in members:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)