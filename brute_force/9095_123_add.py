import sys

dp = [0, 1, 2, 4]

T = int(sys.stdin.readline())
for i in range(4, 12):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for _ in range(T):
    print(dp[int(sys.stdin.readline())])