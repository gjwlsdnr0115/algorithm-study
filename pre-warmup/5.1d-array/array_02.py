data = []
num_dict = {}

while True:
    try:
        data.append(int(input()))
    except:
        break

for i in range(len(data)):
    num_dict[data[i]] = i

data.sort()
print(data[-1])
print(num_dict[data[-1]]+1)