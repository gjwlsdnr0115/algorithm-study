import sys
INF = sys.maxsize

input = sys.stdin.readline

# get input cases
T = int(input())
cases = []
for _ in range(T):
    cases.append(list(map(int, input().split())))


# init dp mem
dp = [[0, 0, 0] for _ in range(T)]
ans = INF


if T == 1:
    print(min(cases[0]))
else:

    for start in range(3):
        for i in range(3):
            if start==i:
                dp[0][i] = cases[0][i]
            else:
                dp[0][i] = INF

        for i in range(1, T):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cases[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cases[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cases[i][2]

        for i in range(3):
            if start==i:
                continue
            ans = min(ans, dp[T-1][i])


    print(ans)