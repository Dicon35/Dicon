class Student:
    amount_of_students = 0

    def __init__(self, name="Human"):
        self.name = name
        Student.amount_of_students = 1


    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

denis = Student("Denis")
roman = Student("Roman")

denis.set_name("Denis")
denis.get_name()

roman.get_name()
