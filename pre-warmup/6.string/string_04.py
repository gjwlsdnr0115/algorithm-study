n = int(input())
for i in range(n):
    data = input().split()
    repeat_num = int(data[0])
    string = data[1]

    s = ''
    for c in string:
        s += c*repeat_num
    print(s)