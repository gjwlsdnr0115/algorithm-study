n = int(input())

if n==1:
    print(1)
else:
    count = 2
    current = 7
    while True:
        if current >= n:
            break
        else:
            current += (count*6)
            count += 1
    print(count)