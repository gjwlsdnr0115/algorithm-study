from collections import deque

dq = deque([])  # for tags
stack = []  # for words
word = input()
ans = ''

tag = False

for c in word:
    if not tag:
        if c=='<':  # start of tag
            size = len(stack)  # empty stack
            for _ in range(size):
                ans += stack.pop()

            tag = True
            dq.append(c)  # add to deque
        elif c==' ':  # end of word
            size = len(stack)  # empty stack
            for _ in range(size):
                ans += stack.pop()
            ans += ' '
        else:  # middle of word
            stack.append(c)

    else:
        if c=='>':  #  end of tag
            tag = False
            size = len(dq)  # empty deque
            for _ in range(size):
                ans += dq.popleft()
            ans += '>'
        else:  # middle of tag
            dq.append(c)

if len(stack)!=0:  # empty remaining stack
    size = len(stack)
    for _ in range(size):
        ans += stack.pop()
print(ans)