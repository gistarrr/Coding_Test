# 개미 전사
x = int(input())
storage = list(map(int, input().split()))

dp = [0]*100
dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])

for i in range(2, x):
    dp[i] = max(storage[i]+dp[i-2], dp[i-1])

print(dp[x-1])