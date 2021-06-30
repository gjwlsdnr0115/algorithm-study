import sys
n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()
for d in data:
    print(d[0],d[1])