n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    student_num = data[0]
    avg = sum(data[1:])/student_num
    count = 0
    for j in range(1, student_num+1):
        if data[j]>avg:
            count += 1
    print('{:.3f}%'.format(count/student_num*100))