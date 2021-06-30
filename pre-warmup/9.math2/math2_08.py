x_dict = {}
y_dict = {}

for _ in range(3):
    a, b = map(int, input().split())
    x_dict[a] = x_dict.get(a, 0) + 1
    y_dict[b] = y_dict.get(b, 0) + 1


for key in x_dict.keys():
    if x_dict[key]==1:
        print(key, end=' ')
for key in y_dict.keys():
    if y_dict[key]==1:
        print(key)