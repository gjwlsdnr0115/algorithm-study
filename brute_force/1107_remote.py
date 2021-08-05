import sys
input = sys.stdin.readline

N = int(input())
b = int(input())

remote = {str(i) for i in range(10)}

if b > 0:
    remote -= set(map(str, input().split()))

current_channel = 100

min_cnt = abs(current_channel - N)

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in remote:
            break
        elif j == len(str(channel)) - 1:
            min_cnt = min(min_cnt, abs(channel - N) + len(str(channel)))

print(min_cnt)