import sys
import math
from functools import reduce


N, S = map(int, sys.stdin.readline().split())

A_list = [int(n) for n in sys.stdin.readline().split()]

A_distance = list(set(abs(a-S) for a in A_list))
print(reduce(math.gcd, A_distance))


# alternative, slower

d = min(A_distance)
for i in range(len(A_distance)):
    d = math.gcd(A_distance[i], d)
print(d)