N = int(input())

for _ in range(N):
    p_string = input()
    stack = []
    vps = True
    for p in p_string:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0:
                prev = stack.pop()
                if prev != '(':
                    vps = False
                    break
            else:
                vps = False
                break
    if len(stack) != 0:
        vps = False

    if vps:
        print('YES')
    else:
        print('NO')