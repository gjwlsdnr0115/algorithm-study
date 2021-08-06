from itertools import combinations

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
com = combinations(nums, m)

for c in com:
    for num in c:
        print(num, end=' ')
    print()