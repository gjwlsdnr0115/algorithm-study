def get_line(num):
    acc = 1
    count = 1
    while True:
        if acc < num:
            count +=1
            acc += count
        else:
            break
    return count, acc - count

n = int(input())
line, acc = get_line(n)

if line%2==0:
    numerator = 1
    denominator = line
    for _ in range(n-acc-1):
        numerator += 1
        denominator -= 1
    print('{}/{}'.format(numerator, denominator))
else:
    numerator = line
    denominator = 1
    for _ in range(n-acc-1):
        numerator -= 1
        denominator += 1
    print('{}/{}'.format(numerator, denominator))
