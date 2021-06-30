def get_dial_num(c):
    if c < 'D':
        return 2
    elif c < 'G':
        return 3
    elif c < 'J':
        return 4
    elif c < 'M':
        return 5
    elif c < 'P':
        return 6
    elif c < 'T':
        return 7
    elif c < 'W':
        return 8
    else:
        return 9

s = input()
total = 0
for c in s:
    total += get_dial_num(c) + 1
print(total)


