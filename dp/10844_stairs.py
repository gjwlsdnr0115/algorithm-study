import sys
input = sys.stdin.readline

m = 100
mod = 1000000000

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(m+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]

for i in range(3, m+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    for j in range(10):
        dp[i][j] %= mod

print(sum(dp[int(input())])%mod)