N = int(input())

five = int(N/5)
three = 0

while True:
    if (N-five*5)%3==0:
        result = five + int((N-five*5)/3)
        print(result)
        break
    if five*5+three*3==N:
        print(five+three)
        break
    else:
        if five > 0:
            five -= 1
        three += 1
    if three*3 > N:
        print(-1)
        break