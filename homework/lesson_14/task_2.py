"""Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

```

def stop_words(words: list):

    pass



@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"



assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

```"""
from functools import wraps


def stop_words(words: list):
    def stop_word_searcher(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            str1 = func(*args, **kwargs)
            for word in words:
                if word in str1:
                    str1 = str1.replace(word, "*")
            return str1
        return wrap
    return stop_word_searcher



@stop_words(["coca-cola", "VW"])
def create_slogan(name: str) -> str:
    return f"{name} drinks coca-cola in his brand new VW!"


if __name__ == '__main__':
    print(create_slogan("Dante"))
    assert create_slogan("Dante") == "Dante drinks * in his brand new *!"
