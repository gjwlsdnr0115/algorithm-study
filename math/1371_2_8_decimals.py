
# time over
two = input()

decimal = 0
length = len(two)

for i in range(length):
    decimal += int(two[i]) * 2**(length-1-i)

digits = 1
d = decimal
n = 8
while n <= d:
    n = n*8
    digits += 1

ans = ''
for i in range(digits-1, 0, -1):
    ans += str(d//8**i)
    d = d%8**i
ans += str(d)
print(ans)

# alternative

n = input()
print(oct(int(n, 2))[2:])