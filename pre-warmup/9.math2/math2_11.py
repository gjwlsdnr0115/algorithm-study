import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif r1 > distance+r2:
        print(0)
    elif r1 == distance+r2:
        print(1)
    elif r2 > distance+r1:
        print(0)
    elif r2 == distance+r1:
        print(1)
    else:
        if distance > r1+r2:
            print(0)
        elif distance == r1+r2:
            print(1)
        else:
            print(2)