def is_end(n):
    s = str(n)
    if '666' in s:
        return True

n = int(input())
current = 0
num = 666
while current < n:
    if is_end(num):
        current += 1
    num+=1
print(num-1)