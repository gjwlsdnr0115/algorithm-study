import sys

N = int(sys.stdin.readline())
equation = sys.stdin.readline().strip()

num_dict = {}

# make dictionary of alphabet: num
A = ord('A')
for i in range(A, A+N):
    num_dict[chr(i)] = int(sys.stdin.readline())


stack = []

for c in equation:
    if c == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif c == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif c == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif c == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    else:
        stack.append(num_dict[c])

print('%.2f'%stack[0])