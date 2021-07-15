def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
