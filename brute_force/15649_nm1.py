from itertools import permutations

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
per = permutations(nums, m)

for p in per:
    for num in p:
        print(num, end=' ')
    print()