# class Student:
#     amount_of_students = 0
#
#     def __init__(self, name="Human"):
#         self.name = name
#         Student.amount_of_students = 1
#
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(self.name)
#
# denis = Student("Denis")
# roman = Student("Roman")
#
# denis.set_name("Denis")
# denis.get_name()
#
# roman.get_name()
#
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -=3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_avive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion...")
            self.alive = False
        elif self.progress > 5:
            print("Passed exams")
            self.alive = False


    def day(self):
        print(f"Glandess - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + "life"
        print(f"{day:^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.day()
        self.is_avive()


denis = Student("Denis")

for day in range (1, 366):
    if denis.alive == False:
        break
    denis.live(day)



