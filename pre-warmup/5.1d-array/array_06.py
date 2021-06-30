n = int(input())

for i in range(n):
    total = 0
    count = 0

    s = input()
    for c in s:
        if c == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)