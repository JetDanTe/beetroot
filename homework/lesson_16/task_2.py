"""Task 2

Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,
 `end`, and optional step. Tips: See the documentation for `range` function"""

class Range:

    def __init__(self, start, stop, step):
        self.step = step
        self.stop = stop
        self.start = start

    def __iter__(self):
        self.start -= self.step
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        raise StopIteration



if __name__ == '__main__':
    dante = Range(1, 100, 18)
    for i in dante:
        print(i)
