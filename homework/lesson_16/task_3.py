"""Task 3

Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
elements using square brackets syntax."""

class Rumbottle:

    def __init__(self, iterable: str, ind=0):
        self.iterable = iterable
        self.ind = ind

    def __iter__(self):
        print(f"We have {len(self.iterable[self.ind:])} bottles of Rum!")
        return self

    def __next__(self):
        if self.ind < len(self.iterable):
            old_ind = self.ind
            self.ind += 1
            return f" Yo ho ho and {len(self.iterable[old_ind:])} bottles of Rum!"
        else:
            print(f"We are all drunk!")
            raise StopIteration

if __name__ == '__main__':
    dante = Rumbottle("olololol ya voditel nlo", 3)
    for i in dante:
        print(i)