from collections import deque

dq = deque([])
ans = []

N, K = map(int, input().split())

for i in range(1, N+1):  # add to deque
    dq.append(i)

while len(dq) > 0:
    for _ in range(K-1):
        dq.append(dq.popleft())  # pop and add back to deque for K-1 times
    ans.append(dq.popleft())  # pop next num

print('<', end='')
for i in range(N-1):
    print(ans[i], end=', ')
print(ans[-1], end='>')