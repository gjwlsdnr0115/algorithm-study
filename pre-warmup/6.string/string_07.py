def reverse_string(s):
    return s[::-1]

a, b = map(int, reverse_string(input()).split())
if a > b:
    print(a)
else:
    print(b)