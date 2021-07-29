import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = seq.copy()
for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[j] + seq[i], dp[i])

print(max(dp))