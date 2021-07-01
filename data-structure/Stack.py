class Stack:
    def __init__(self):
        self.datas = []

    def __len__(self):
        return len(self.datas)

    def __str__(self):
        return str(self.datas[::1])

    def isEmpty(self):
        return len(self.datas)==0

    def push(self, data):
        self.datas.append(data)

    def pop(self):
        if not self.isEmpty():
            data = self.datas.pop()
            return data
        else:
            return -1

    def size(self):
        return len(self.datas)

    def top(self):
        if not self.isEmpty():
            return self.datas[-1]
        else:
            return -1

    def clear(self):
        self.datas = []

    def contain(self, data):
        return data in self.datas