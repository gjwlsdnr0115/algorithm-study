def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

m = int(input())
n = int(input())

primes = []
for i in range(m, n+1):
    if is_prime(i):
        primes.append(i)

if len(primes)==0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))