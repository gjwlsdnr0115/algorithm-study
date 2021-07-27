N = int(input())

mod = 9901

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
    dp[i] = (2*dp[i-1] + dp[i-2]) % mod

print(dp[N])