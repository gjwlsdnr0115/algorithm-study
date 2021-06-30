data = set()

while True:
    try:
        mod = int(input())%42
        data.add(mod)

    except:
        break

print(len(data))