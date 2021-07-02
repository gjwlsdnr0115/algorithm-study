'''
1.
# Time over
import sys

text = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
ops = []


cursor = len(text)-1

for _ in range(N):
    ops.append(sys.stdin.readline().split())

for op in ops:
    if op[0] == 'L':
        if cursor!=-1:
            cursor -= 1
    elif op[0] == 'D':
        if cursor != len(text)-1:
            cursor += 1
    elif op[0] == 'B':
        if cursor != -1:
            text = text[:cursor] + text[cursor+1:]
            cursor -= 1
    else:
        text = text[:cursor+1] + op[1] + text[cursor+1:]
        cursor += 1

print(text)
'''

# 2.

import sys

stack1 = list(sys.stdin.readline().strip())  # left of cursor
stack2 = []  # right of cursor

N = int(sys.stdin.readline())
ops = []


for _ in range(N):
    ops.append(sys.stdin.readline().strip())

for op in ops:
    if op[0] == 'L':
        if len(stack1)!=0:
            stack2.append(stack1.pop())  # move cursor to left
    elif op[0] == 'D':
        if len(stack2) != 0:
            stack1.append(stack2.pop())  # # move cursor to right
    elif op[0] == 'B':
        if len(stack1)!=0:
            stack1.pop()
    else:
        stack1.append(op[2])

print(''.join(stack1 + list(reversed(stack2))))