import sys

# make dictionary for alphabet digits
alph_to_decimal = {}
ord_A = ord('A')  # 65

for i in range(ord_A, ord_A+26):
    alph_to_decimal[chr(i)] = i-55

# get input
inputs = sys.stdin.readline().split()
N = inputs[0]
d = int(inputs[1])


value = 0
N = N[::-1]  # reverse string

# add total value
for i in range(len(N)):
    if N[i].isalpha():
        value += (d ** i) * alph_to_decimal[N[i]]
    else:
        value += (d ** i) * int(N[i])

print(value)