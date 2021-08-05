import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

while True:

    if e == s and s == m:
        break

    if min(e, s, m) == e:
        e += 15
    elif min(e, s, m) == s:
        s += 28
    else:
        m += 19

print(e)
