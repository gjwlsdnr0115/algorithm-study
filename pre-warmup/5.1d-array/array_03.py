a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
digits = [int(d) for d in str(mul)]

for i in range(10):
    print(digits.count(i))