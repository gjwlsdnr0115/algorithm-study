dp = [0, 1, 2]
n = int(input())

# tiles for 2 x n = 2 x n-2 + 2 x n-2
for i in range(3, n+1):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n]%10007)
