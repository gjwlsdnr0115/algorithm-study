import sys

# make dictionary for alphabet digits
decimal_to_alph = {}
ord_A = ord('A')  # 65

for i in range(ord_A, ord_A+26):
    decimal_to_alph[i-55] = chr(i)

# get input
N, d = map(int, sys.stdin.readline().split())

# convert to d decimals
digits = []
while N!=0:
    digits.append(N%d)
    N //= d

# convert to alphabet and print result
ans = ''
for i in range(len(digits)-1, -1, -1):
    if digits[i] > 9:
        ans += decimal_to_alph[digits[i]]
    else:
        ans += str(digits[i])
print(ans)
