def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True


n = int(input())
data = list(map(int, input().split()))
count = 0
for i in range(n):
    if is_prime(data[i]):
        count += 1
print(count)