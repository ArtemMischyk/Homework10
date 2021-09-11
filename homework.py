"""class Homework"""

class Homework:
    """Homework class"""
    def __init__(self, name, age, assignment_name, assignment_subject, grade,):
        """Homework constructor"""
        self.name = name
        self.age = age
        self.assignment_name = assignment_name
        self.assignment_subject = assignment_subject
        self.grade = grade

    def description(self):
      return f"{self.name}, age: {self.age}, assignment_name: {self.assignment_name}, subject: {self.assignment_subject}, grade: {self.grade}"

hw1 = Homework("Nikolai", 14,"Tuples", "Python", 80)
hw2 = Homework("Jack", 12, "Lists", "Python", 100)
hw3 = Homework("Thomas", 16, "Function", "Python", 88)
hw4 = Homework("George", 17, "Dictionaries", "Python", 75)
hw5 = Homework("Sophia", 15, "Strings", "Python", 63)

homeworks = [hw1, hw2, hw3, hw4, hw5]

def show_homeworks(homeworks):
    for h in homeworks:
        print(h.description())

print("Initial")
show_homeworks(homeworks)

def foo():
    """Some func"""