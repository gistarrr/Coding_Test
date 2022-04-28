num_st = int(input())
stairs = []
for _ in range(num_st):
    stairs.append(int(input()))

dp = [0] * (num_st)

if num_st == 1 :
    print(stairs[0])
elif num_st == 2 :
    print(stairs[0] + stairs[1])
else :
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, num_st):
        dp[i] = max(dp[i-2]+ stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    
    print(dp[num_st-1])