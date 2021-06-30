import math
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    margin = c - b
    required_sold = math.floor(a/margin) + 1
    print(required_sold)