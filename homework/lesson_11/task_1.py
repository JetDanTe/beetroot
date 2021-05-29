"""Task 1

School

Make a class structure in python representing people at school. Make a base class called Person, a class called
Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong
to different classes, and keep in mind which are common and which are not. For example, the name should be a Person
attribute, while salary should only be available to the teacher.
"""

class Person:

    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def show_inf(self):
        return(f"Person's name is {self._first_name} {self._last_name} and he is {self._age} years old!")

class Student(Person):

    def __init__(self, first_name, last_name, age, course, course_name):
        super().__init__(first_name, last_name, age)
        self.course_name = course_name
        self.course = course

    def show_student_info(self):
        return(f"He learning at {self.course} course on {self.course_name}")

class Teacher(Person):

    def __init__(self, first_name, last_name, age, subject, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.subject = subject

    def show_teacher_info(self):
        return(f"He is teaching {self.subject} and has salary {self.salary} per month")



dante = Student("Dante", "Alighieri", 26, '5', "IB")
sparda = Teacher("Sparda", "Alighieri", 26, "History", 1000)
print(dante.show_inf())
print(dante.show_student_info())
print(sparda.show_inf())
print(sparda.show_teacher_info())
