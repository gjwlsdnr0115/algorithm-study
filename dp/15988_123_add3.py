import sys

input = sys.stdin.readline

# get test cases
T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

# set markers
largest = max(cases)
mod = 1000000009

# init dp mem
dp = [0] * (largest+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, largest+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= mod

# print
for c in cases:
    print(dp[c])
