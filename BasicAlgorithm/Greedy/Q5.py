# 볼링공 고르기
N, M = map(int, input().split())
bowling = list(map(int, input().split()))
result = 0
for i in range(len(bowling)-1):
    for j in range(i+1, len(bowling)):
        if bowling[i] != bowling[j]:
            result += 1

print(result)
