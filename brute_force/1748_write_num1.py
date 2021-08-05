
n = int(input())

digits = len(str(n))

ans = 0

for i in range(1, digits):
    ans += 9*(10**(i-1))*i

ans += digits*(n-(10**(digits-1)-1))

print(ans)