T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y-x
    count = 0
    move = 1
    move_agg = 0
    while move_agg < dist:
        count += 1
        move_agg += move
        if count%2==0:
            move += 1
    print(count)