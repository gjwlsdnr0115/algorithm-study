import sys
n = int(input())

data = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    data.append([y, x])

data.sort()
for d in data:
    print(d[1],d[0])