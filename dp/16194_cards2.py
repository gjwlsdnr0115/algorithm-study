import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

dp = [0, P[0]]
for i in range (2, N+1):
    temp = []
    for j in range(1, i):
        temp.append(dp[j] + P[i-1-j])
    temp.append(P[i-1])
    dp.append(min(temp))
print(dp[N])