"""Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds
    the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

```

class Library:

    pass



class Book:

    pass



class Author:

    pass

```

"""

class Author:

    def __init__(self, first_name, last_name, birt_date, country):
        self.country = country
        self.birt_date = birt_date
        self.last_name = last_name
        self.first_name = first_name
        self.books = []

    def new_book(self, name, year):
        book = Book(name, year, self)
        self.books.append(book)
        return book

    def __str__(self):
        return f"Author {self.first_name} {self.last_name} written {self.books}, {len(self.books)} books!"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Book:
    books_counter = 0
    def __init__(self, name, year, author: "Author"):
        self.author = author
        self.year = year
        self.__name = name
        self.__class__.books_counter += 1


    def __repr__(self):
        return f"{self.__name}"




class Library:


    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []


    def add_book(self, book: Book):
        self.books.append(book)
        self.authors.append(book.author)


    def add_author(self,):
        pass

    def group_by_author(self, author: Author):
        return author.__str__()

    def group_by_year(self, year: str):
        year_list = []
        for book in self.books:
            if year in book.year:
                year_list.append(book)
        return year_list


    def __str__(self):
        return f"In the library {self.name} are {len(self.books)} books: {self.books}"


    def __repr__(self):
        return self.__str__()

lib1 = Library("Babylon")
dante = Author("Dante", "Alighieri", "18.04.1995", "Ukraine")
vergil = Author("Vergil", "Sparda", "11.03.1996", "UA")
sparda = Author("Sparda", "Devil", "13.10.1502", "UK")

vb1 = vergil.new_book("The RE:location", "2021")
vb2 = vergil.new_book("Python with robots for kids", "2021")
db1 = dante.new_book("The great dance", "2021")
db2 = dante.new_book("Teodor", "2021")
sb1 = sparda.new_book("C++ for kids with robots", "1603")
sb2 = sparda.new_book("C++ for buddies with robots", "1656")

lib1.add_book(vb1)
lib1.add_book(vb2)
lib1.add_book(db1)
lib1.add_book(db2)
lib1.add_book(sb1)
lib1.add_book(sb2)

print(lib1.group_by_author(sparda))
print(lib1.group_by_year("2021"))
print(lib1)

