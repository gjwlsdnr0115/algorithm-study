import sys

while True:
    s = sys.stdin.readline().rstrip('\n')  # only remove '\n' at the end
    up = 0
    low = 0
    num = 0
    space = 0

    if not s:
        break
    for c in s:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isnumeric():
            num += 1
        elif c.isspace():
            space += 1
    print(low, up, num, space)
