from collections import deque
import sys

N = int(input())
dq = deque([])

for _ in range(N):
    op = sys.stdin.readline().split()

    if op[0]=='push_back':
        dq.append(int(op[1]))
    elif op[0]=='push_front':
        dq.appendleft(int(op[1]))
    elif op[0]=='pop_back':
        if len(dq)!=0:
            print(dq.pop())
        else:
            print(-1)
    elif op[0]=='pop_front':
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    elif op[0]=='size':
        print(len(dq))
    elif op[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif op[0]=='front':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif op[0]=='back':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)

