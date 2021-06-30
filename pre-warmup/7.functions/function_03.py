def hansu(a):
    digits = [int(d) for d in str(a)]
    if len(digits) > 3:
        return False
    elif len(digits) == 3:
        if digits[1] - digits[0] == digits[2] - digits[1]:
            return True
        else:
            return False
    return True

count = 0
n = int(input())
for i in range(1, n+1):
    if hansu(i):
        count += 1
print(count)