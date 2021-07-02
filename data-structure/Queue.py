# 1. use deque
# add, del: O(1)

from collections import deque

# deque init
dq = deque([])

# add data

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)  # deque([1, 2, 3, 4])

print(dq.popleft())  # 1
print(dq.popleft())  # 2
print(dq.popleft())  # 3
print(dq.popleft())  # 4
print(dq)  # deque([])

# 2. use queue

import queue

# queue init
q = queue.Queue()

# add data
q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())  # 1
print(q.get())  # 2
print(q.get())  # 3
print(q.get())  # 4


l = [1, 2, 3, 4]
l3 = l + l.reverse()