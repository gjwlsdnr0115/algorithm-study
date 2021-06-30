data = input().split()
a = data[0]
b = data[1]

if len(a)<len(b):
    difference = len(b) - len(a)
    a = '0'*difference + a
else:
    difference = len(a) - len(b)
    b = '0' * difference + b
c = ''
up = 0
for i in range(len(a)-1, -1, -1):
    add = int(a[i]) + int(b[i]) + up
    up = 0
    if add >= 10:
        add -= 10
        c = str(add)+c
        up = 1
    else:
        c = str(add) + c

if up==1:
    c = '1'+c
print(c)
