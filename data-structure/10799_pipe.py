import sys

string = sys.stdin.readline()
string = string.replace('()', '*')  # replace laser location with *

stack = []
total = 0

for c in string:
    if c == '(':  # new pipe
        stack.append(c)
    elif c == ')':  # end of pipe
        stack.pop()
        total += 1
    else:  # cut pipe
        total += len(stack)

print(total)