from itertools import combinations
import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

T = int(input())

for _ in range(T):
    data = sys.stdin.readline().split()
    nums = [int(data[i]) for i in range(1, len(data))]  # first element is number of nums

    gcds = []
    comb = combinations(nums, 2)
    for (a, b) in comb:
        gcds.append(gcd(a, b))  # add gcd of all combinations
    print(sum(gcds))


