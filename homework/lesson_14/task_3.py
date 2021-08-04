"""Write a decorator `arg_rules` that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise,
return the result.

```

def arg_rules(type_: type, max_length: int, contains: list):

    pass



@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"



assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'"""

def arg_rules(type_: type, max_length: int, contains: list):
    def validator(func):
        #@wraps(func)
        def wrap(*args, **kwargs):
            if not type(*args, **kwargs) == type_:
                print(f"The type of slogan must be {type_} - given {type(*args, **kwargs)}")
                return False
            if not max_length >= len(*args, **kwargs):
                print(f"The length of the input must be {max_length} max - given {len(*args, **kwargs)}")
                return False
            for i in contains:
                if not i in str(*args, **kwargs):
                    print(f"The name must contain {contains} - given {str(*args, **kwargs)} ")
                    return False
            return func(*args, **kwargs)
        return wrap
    return validator

@arg_rules(type_= str, max_length = 15, contains = ['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

if __name__ == '__main__':
    print(create_slogan("johndoe05@gmail.com"))
    print(create_slogan("S@SH05"))
    print(create_slogan(33))
    print(create_slogan("dante"))
