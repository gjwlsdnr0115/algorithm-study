S = input()

# make alphabet count dictionary
alphabet_count = {}
A = ord('a')
for i in range(A, A+26):
    alphabet_count[chr(i)] = 0

# add count for each character in string
for c in S:
    alphabet_count[c] = alphabet_count.get(c, 0) + 1

# print dictionary
for key in alphabet_count.keys():
    print(alphabet_count[key], end=' ')