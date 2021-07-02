N = int(input())

sequence = []
stack = []
answer = []
valid = True

for _ in range(N):
    sequence.append(int(input()))

idx = 0
stack = [0]
pushed = 0


while idx < N:
    next_seq = sequence[idx]
    if stack[-1] < next_seq:  # push until next sequence
        for _ in range(next_seq-pushed):
            pushed += 1
            stack.append(pushed)
            answer.append('+')
        stack.pop()
        answer.append('-')  # pop sequence
    elif stack[-1] == next_seq:  # pop next sequence
        stack.pop()
        answer.append('-')

    else:  # invalid if has to pop more than twice
        valid = False
        break
    idx += 1

if valid:
    for i in range(len(answer)):
        print(answer[i])
else:
    print('NO')