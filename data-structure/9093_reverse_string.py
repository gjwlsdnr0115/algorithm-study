import sys
N = int(input())

for _ in range(N):
    words = sys.stdin.readline().split()
    for word in words:
        print(word[::-1], end=' ')

        #------ slower
        # stack = []
        # for w in word:
        #     stack.append(w)
        # for i in range(len(word)):
        #     print(stack.pop(), end='')
        # print(' ', end='')