n = int(input())
data = list(map(int, input().split()))
data_unique = list(set(data))
data_unique.sort()

data_idx = {}

for i in range(len(data_unique)):
    data_idx[data_unique[i]] = i

for d in data:
    print(data_idx[d], end=' ')

