import sys
decimal = int(sys.stdin.readline())

ans = ''
if decimal == 0:
    print(0)
else:
    while decimal != 0:
        if decimal%(-2) == 0:
            ans += '0'
            decimal //= (-2)
        else:
            ans += '1'
            decimal = decimal//(-2) + 1
    print(ans[::-1])

