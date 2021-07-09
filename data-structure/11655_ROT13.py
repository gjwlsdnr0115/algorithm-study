S = input()

upper_bound = ord('Z')
lower_bound = ord('z')
ans = ''

for c in S:
    if c.isupper():  # uppercase
        c_ord = ord(c)
        c_ord += 13
        if c_ord > upper_bound:  # passed 'Z'
            c_ord -= 26
        ans += chr(c_ord)
    elif c.islower():  # lowercase
        c_ord = ord(c)
        c_ord += 13
        if c_ord > lower_bound:  # passed 'z'
            c_ord -= 26
        ans += chr(c_ord)
    else:  # not alphabet
        ans += c

print(ans)