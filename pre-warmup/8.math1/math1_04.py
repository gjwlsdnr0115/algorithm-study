a, b, v = map(int, input().split())

daily = a-b
result = (v-b)/daily
if result == int(result):
    print(int(result))
else:
    print(int(result)+1)