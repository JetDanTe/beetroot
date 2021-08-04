"""Task 1

File Context Manager class

Create your own class, which can behave like a built-in function `open`. Also, you need to extend its functionality
with counter and logging. Pay special attention to the implementation of `__exit__` method, which has to cover all the
requirements to context managers mentioned here:

https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager

https://docs.python.org/3.7/reference/compound_stmts.html#with"""

import datetime

class Dante:
    __counter = 0

    @classmethod
    def get_num_of_usage(cls):
        return cls.__counter

    def __enter__(self):
        Dante.__counter += 1
        self.write_log("File is opened")
        return self

    def write_log(self, log):
        with open("logs.log", "a") as l:
            l.writelines(f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}: {log}, {self.__counter} times\n")
            l.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write_log("File is closed")
        return None

if __name__ == '__main__':
    with Dante() as d:
        print(d.get_num_of_usage())

    with Dante() as d:
        print(d.get_num_of_usage())

    with Dante() as d:
        print(d.get_num_of_usage())