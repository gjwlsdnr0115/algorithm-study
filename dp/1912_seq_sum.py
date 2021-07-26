import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]*n

# 지금까지 이어저 오는 연속된 합 or 새로 시작
for i in range(1, n):
    dp[i] = max(dp[i-1] + seq[i], seq[i])

print(max(dp))