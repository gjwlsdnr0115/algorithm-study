import sys
input = sys.stdin.readline

m = 90

dp = [[0, 0] for _ in range(m+1)]
dp[1] = [0, 1]
dp[2] = [1, 0]
dp[3] = [1, 1]

for i in range(4, m+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[int(input())]))
