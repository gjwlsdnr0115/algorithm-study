import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

rev_seq = seq[::-1]

dp = [1]*n
rev_dp = [1]*n

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
        if rev_seq[j] < rev_seq[i]:
            rev_dp[i] = max(rev_dp[i], rev_dp[j] + 1)

result = []
for i in range(n):
    result.append(dp[i] + rev_dp[n-i-1] -1)
print(max(result))