import sys

N = int(sys.stdin.readline())
queue = []


for _ in range(N):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        queue.insert(0, op[1])
    elif op[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

