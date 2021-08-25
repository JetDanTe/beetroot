"""Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module. Make the class have
two global variables, one called counter set to 0, and another called rounds set to 100.000. Now implement the run()
method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and for each time increments
the value of the counter by 1. Create 2 instances of the thread and start them, then join them and check the result of
the counter, it should be 200.000, right? Run it a couple of times and consider some different reasons why you get the
answer that you get.

"""
import threading

counter = 0
lock = threading.Lock()
class Counter(threading.Thread):
    rounds = 100000

    def run(self):
        global counter
        for i in range(self.rounds):
            with lock:
                counter += 1


if __name__ == '__main__':
    dante1 = Counter()
    dante2 = Counter()
    dante1.start()
    dante2.start()
    dante1.join()
    print(counter)
    dante2.join()
    print(counter)

