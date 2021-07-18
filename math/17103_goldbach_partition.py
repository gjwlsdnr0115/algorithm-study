import sys

def get_eratos(N):
    nums = [True for _ in range(N)]
    for i in range(2, int(N**0.6)+1):
        if nums[i] == True:
            for j in range(i*2, N, i):
                if nums[j]==True:
                    nums[j]=False
    return nums

r = 1000000  # max test case
primes = get_eratos(r)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())

    if n==4:  # only applies for (2, 2)
        print(1)
    else:
        count = 0
        half = n//2+1  # only count until half

        for i in range(3, half, 2):
            if primes[i] and primes[n-i]:  # both are primes
                count += 1

        print(count)