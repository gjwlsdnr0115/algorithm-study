def is_prime(a):
    if a <= 1:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a%i==0:
                return False

        return True

N = int(input())
nums = input().split()

count = 0
for n in nums:
    if is_prime(int(n)):
        count += 1
print(count)