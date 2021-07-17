def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
chars = [c for c in str(factorial(n))]  # get factorial result as list of chars

count = 0
for _ in range(len(chars)):  # check from back if zero
    if chars.pop()=='0':
        count += 1
    else:
        break

print(count)


# 2.

'''
5의 몫을 계속 더한것과 같다
'''

count = 0
while n >= 5:
    count += n // 5
    n //= 5

print(count)