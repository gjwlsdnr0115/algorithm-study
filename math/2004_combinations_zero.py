def two_count(n):  # count number of multiplied 2s in n
    count = 0
    while n >= 2:
        count += n//2
        n //= 2
    return count

def five_count(n): # count number of multiplied 5s in n
    count = 0
    while n >= 5:
        count += n//5
        n //= 5
    return count

n, m = map(int, input().split())

print(min(two_count(n)-two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m)))