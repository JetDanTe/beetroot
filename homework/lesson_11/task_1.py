"""Task 1

School

Make a class structure in python representing people at school. Make a base class called Person, a class called
Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong
to different classes, and keep in mind which are common and which are not. For example, the name should be a Person
attribute, while salary should only be available to the teacher.
"""

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_inf(self):
        return(f"Person's name is {self.first_name} {self.last_name} and it is {self.age} years old!")

class Student(Person):

    def __init__(self, course, marks):
        super.__init__()
        self.marks = marks
        self.course = course

    def show_student_info(self):
        return(f"Student name is {}. He lerarning at {} ans has {}")


dante = Person("Dante", "Alighieri", 26)
dante_student = Student('IB', [5,5,5,5,5,5])
print(dante.show_inf())
print(dante_student.show_student_info())

