def get_self_num(cons):
    result = 0
    s_cons = str(cons)
    for c in s_cons:
        result += int(c)
    return result + cons

total = set()
start = 1
while True:
    new = get_self_num(start)
    if new <= 15000:
        total.add(new)
    else:
        break

    start += 1

for i in range(1, 10001):
    if i not in total:
        print(i)