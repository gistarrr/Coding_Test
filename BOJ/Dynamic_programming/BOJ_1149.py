num_house = int(input())
house_arr = []

for _ in range(num_house):
    house_arr.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(num_house)]
dp[0] = house_arr[0]

for i in range(1, num_house):
    dp[i][0] = min(dp[i-1][1]+house_arr[i][0], dp[i-1][2]+house_arr[i][0])
    dp[i][1] = min(dp[i-1][0]+house_arr[i][1], dp[i-1][2]+house_arr[i][1])
    dp[i][2] = min(dp[i-1][0]+house_arr[i][2], dp[i-1][1]+house_arr[i][2])

print(min(dp[-1]))