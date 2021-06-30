import sys
from collections import Counter

n = int(input())
data = []
count = {}
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
print('%.f'%(sum(data)/n))
print(data[n//2])

k = Counter(data).most_common()
if len(data) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(data[0])
print(data[-1]-data[0])