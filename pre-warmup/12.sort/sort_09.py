import sys
n = int(input())

people = []

for _ in range(n):
    data = sys.stdin.readline().split()
    age = int(data[0])
    people.append([age, data[1]])

people.sort(key=lambda item: item[0])
for person in people:
    print(person[0], person[1])