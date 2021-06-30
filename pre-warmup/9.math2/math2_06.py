# n 이하의 소수 찾기
def prime_list(n):
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i+i, n, i):  # i 이후 i의 배수는 False로 판
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

def prime_add(n):
    plist = prime_list(n)
    idx = max([i for i in range(len(plist)) if plist[i]<=n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(plist)):
            if plist[i]+plist[j]==n:
                return plist[i], plist[j]

for _ in range(int(input())):
    n = int(input())
    a, b = prime_add(n)
    print('{} {}'.format(a, b))



