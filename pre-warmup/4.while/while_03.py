n = int(input())
answer = n
count = 0

while True:
    if n < 10:
        n = n*10 + n
    else:
        a = n//10
        b = n%10
        add = a+b
        n = b*10+(add%10)
    count += 1
    if answer == n:
        break
print(count)