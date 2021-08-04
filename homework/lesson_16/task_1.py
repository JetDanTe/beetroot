"""Task 1

Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

"""

class EnumerateWithIndex:

    def __init__(self, _iterable, _from=0):
        self._iterable = _iterable
        self._from = _from

    def __iter__(self):
        return self

    def __next__(self):
        if self._from > len(self._iterable):
            raise StopIteration
        else:
            try:
                self._from += 1
                return self._iterable[self._from]
            except:
                Exception("\nIter is ended")


if __name__ == '__main__':
    dante = "6546453674f;wjflkewjfiljwfjepf'jiorej;oaejh"
    for i in EnumerateWithIndex(dante, 2):
        print(i, end="")