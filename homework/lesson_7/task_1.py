"""Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing
the name of your favorite movie. The function should then print “My favorite movie is named {name}”.
 """


def favourite_movie(movie):
    return movie


movie = favourite_movie(input('Hello, enter your favourite movie:\n'))
print(f"Your favourite movie is: {favourite_movie(movie)}")
