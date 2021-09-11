from person import Person

class Student(Person):
    def __init__(self, name, age, subscribed_course):
        super().__init__(name, age)
        self.avarage_grade = 0
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def __str__(self):
        ret = f"{self.name}, age:{self.age}, grade: {self.avarage_grade},  course:{self.subscribed_course}"
        ret = ret +"Homeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t" + str(h) + "\n"
        return ret
    def add_homeworks(self, homework):
        self.homeworks.append(homework)