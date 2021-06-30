t = int(input())
for _ in range(t):
    floor = int(input())
    room = int(input())
    f = [x for x in range(1, room+1)]

    for _ in range(floor):
        for i in range(1, room):
            f[i] += f[i-1]
    print(f[room-1])