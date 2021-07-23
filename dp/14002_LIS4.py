import sys
input = sys.stdin.readline

length = int(input())
seq = list(map(int, input().split()))

dp = [1]*(length)

for i in range(length):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

ans = max(dp)

result = []

for i in range(length-1, -1, -1):
    if dp[i]==ans:
        result.append(seq[i])
        ans -= 1

print(max(dp))
for i in range(len(result)-1, -1, -1):
    print(result[i], end=' ')