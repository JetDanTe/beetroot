"""Task 4

Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method
to extend functionality for saving messages to file

```

class CustomException(Exception):

def __init__(self, msg):

...

```"""

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{msg} \n")


while input("Enter Q for exit. \n".lower()) != "q".lower():
    raise CustomException("Q still not entered")