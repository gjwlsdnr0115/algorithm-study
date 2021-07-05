import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

num_count = {}  # get count of each number
for n in numbers:
    num_count[n] = num_count.get(n, 0) + 1

# create tuple of (num, count)
nums = []
for i in range(len(numbers)):
    nums.append((numbers[i], num_count[numbers[i]]))

stack = []  # push larger numbers
result = []

for i in range(len(nums)-1, -1, -1):  # start from back

    while True:
        if len(stack)==0:  # no larger nums on the right
            result.append((-1, -1))  # match datatype as tuple, only need -1
            stack.append(nums[i])  # push to stack
            break
        else:
            if nums[i][1] < stack[-1][1]:  # most right larger number
                result.append(stack[-1])
                stack.append(nums[i])  # add to stack
                break
            else:
                stack.pop()  # pop until len=0 or found larger number

for i in range(len(result)-1, -1, -1):
    print(result[i][0], end=' ')