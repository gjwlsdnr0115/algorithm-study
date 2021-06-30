from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = combinations(data, 3)
combi = []
for c in result:
    combi.append(sum(c))



for i in range(len(combi)):
    combi[i] -= m
    if combi[i] > 0:
        combi[i] = -m

idx = combi.index(max(combi))
closest = combi[idx]
print(closest+m)