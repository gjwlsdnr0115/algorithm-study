import sys

mem = [0,0,1,1]  # initial values until 3

X = int(sys.stdin.readline())

for i in range(4, X+1):  # start from 4
    mem.append(mem[i-1]+1)  # case [x] = [x-1] +1
    if i%2==0: # case [x] = [x//2] +1
        mem[i] = min(mem[i], mem[i//2]+1)
    if i%3==0: # case [x] = [x//3] +1
        mem[i] = min(mem[i], mem[i//3]+1)
print(mem[X])