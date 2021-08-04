import sys
from itertools import combinations

input = sys.stdin.readline

heights = []
for i in range(9):
    heights.append(int(input()))

com = combinations(heights, 7)
for c in com:
    if sum(c) == 100:
        dwarfs = list(c)
        dwarfs.sort()
        for d in dwarfs:
            print(d)
        break
