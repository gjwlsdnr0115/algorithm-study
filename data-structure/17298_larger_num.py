import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

stack = []  # push larger numbers
result = []

for i in range(len(numbers)-1, -1, -1):  # start from back

    while True:
        if len(stack)==0:  # no larger nums on the right
            result.append(-1)
            stack.append(numbers[i])  # push to stack
            break
        else:
            if numbers[i] < stack[-1]:  # most right larger number
                result.append(stack[-1])
                stack.append(numbers[i])  # add to stack
                break
            else:
                stack.pop()  # pop until len=0 or found larger number

for i in range(len(result)-1, -1, -1):
    print(result[i], end=' ')