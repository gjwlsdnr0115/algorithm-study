class stack:
    def __init__(self):
        self.stack_list = []
    def push(self, data):
        self.stack_list.append(data)
    def pop(self):
        if len(self.stack_list)!=0:
            data = self.stack_list.pop()
            return data
        else:
            return -1
    def size(self):
        return len(self.stack_list)
    def empty(self):
        if len(self.stack_list)!=0:
            return 0
        else:
            return 1
    def top(self):
        if len(self.stack_list)!=0:
            return self.stack_list[-1]
        else:
            return -1

import sys

N = int(input())

s = Stack()
for _ in range(N):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        s.push(op[1])
    if op[0] == 'pop':
        print(s.pop())
    if op[0] == 'size':
        print(s.size())
    if op[0] == 'empty':
        print(s.isEmpty())
    if op[0] == 'top':
        print(s.top())
