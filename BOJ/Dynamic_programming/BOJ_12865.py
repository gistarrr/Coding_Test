N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(K+1):
        if j - W >= 0 :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
        else :
            dp[i][j] = dp[i-1][j]

print(max(dp[-1]))
