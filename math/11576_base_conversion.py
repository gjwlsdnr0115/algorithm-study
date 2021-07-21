import sys

A, B = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())
digits = list(map(int, sys.stdin.readline().split()))

digits.reverse()

# convert value to 10s
tens = 0
for i in range(d):
    tens += (A**i)*digits[i]

# convert to base B
ans = []
while tens != 0:
    ans.append(tens%B)
    tens //= B

# print
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=' ')