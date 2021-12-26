class MyRange:
    ''' This class is Range'''

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.count_value = 1

    def __iter__(self):
        while (self.start - self.stop) * self.step < 0:
            yield self.start
            self.start += self.step

    def __next__(self):
        if self.count_value + self.step >= self.stop:
            raise StopIteration
        self.count_value += self.step
        return self.count_value


if __name__ == "__main__":
    my_range = MyRange(0, 3)
    for i in my_range:
        print(i)

    print()

    for i in MyRange(1, 3):
        print(i, end='')

    print()

    for i in MyRange(1, 6, 2):
        print(i, end='')

    print()

    for i in MyRange(10, -5, -1):
        print(i, end='')

    print()
