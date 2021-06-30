def get_div_sum(n):
    digits = [int(c) for c in str(n)]
    return sum(digits)+n

n = int(input())

current = 1
not_found = True
while current < n:
    if get_div_sum(current) == n:
        not_found = False
        break
    else:
        current += 1

if not_found:
    print(0)
else:
    print(current)