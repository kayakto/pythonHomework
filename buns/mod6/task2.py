class DoubleElement:
    def __init__(self, *lst):
        self.list = list(lst)
        if len(self.list) % 2 != 0:
            self.list.append(None)
        self.index = 0

    def __next__(self):
        if self.index + 1 < len(self.list):
            result = (self.list[self.index], self.list[self.index + 1])
            self.index += 2
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
