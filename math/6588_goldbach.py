def get_eratos(N):
    nums = [True for _ in range(N)]
    for i in range(2, int(N**0.6)+1):
        if nums[i] == True:
            for j in range(i*2, N, i):
                if nums[j]==True:
                    nums[j]=False
    return nums

import sys

r = 1000000
primes = get_eratos(r)

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    else:
        not_found = True
        for i in range(3, r):  # 2 is not needed since n is always even number
            if primes[i]==True:
                if primes[n-i]==True:
                    print('{} = {} + {}'.format(n, i, n-i))
                    not_found = False
                    break
        if not_found:
            print("Goldbach's conjecture is wrong.")

