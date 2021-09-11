#from homework import Homework
import homework
from student import Student
from person import Person

class Course:
    """Course class"""
    pass

class Teacher(Person):
    """Teacher class"""
    def __init__(self, name, age):
        """Teacher constructor"""
        super().__init__(name, age)
        self.courses = []

class Employee(Person):
    """Employee class"""
    def __init__(self, name, age):
        """Employee constructor"""
        super().__init__(name, age)
        self.salary = 0

def show_students(students):
    for s in students:
        print(s)

def sort_by_age(students):
    return sorted(students, key=lambda s: s.age)

def sort_by_grade(students):
    return sorted(students, key=lambda s: s.avarage_grade, reverse=True)


students = [
    Student("Student 1", 12, "Python")
    , Student("Student 2", 16, "Python")
    , Student("Student 3", 15, "Python")
    , Student("Student 4", 14, "Python")
    , Student("Student 5", 18, "Python")
]

#homeworks = [
#    Homework("Homework 1", "Description 1", 2, False)
#    , Homework("Homework 2", "Description 2", 5, False,)
#]

print("Initial")
show_students(students)
print("Sorted by age")
show_students(sort_by_age(students))
print("Sorted by grade")
show_students(sort_by_grade(students))

print(homework.__doc__)
print(homework.Homework.__doc__)
print(homework.Homework.__init__.__doc__)
print(homework.foo.__doc__)