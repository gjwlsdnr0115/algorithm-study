import sys

input = sys.stdin.readline

# get input cases
T = int(input())
cases = []
for _ in range(T):
    cases.append(list(map(int, input().split())))

# init dp mem
dp = [[0, 0, 0] for _ in range(T)]
dp[0] = cases[0]
for i in range(1, T):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cases[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cases[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cases[i][2]


print(min(dp[T-1]))
