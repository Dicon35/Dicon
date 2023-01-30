
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.money = 0
        self.behavior = 0
        self.alive = True



    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -=3
        self.money += 5
        self.behavior += 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.behavior += 5

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money += 3
        self.behavior += 2
    def to_work(self):
        print("I`m working")
        self.money += 7
        self.behavior += 3
        self.progress += 0.15
        self.gladness += 2

    def is_avive(self):
        if self.progress <= -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 4:
            print("Depresion...")
            self.alive = False
        elif self.progress >= 5:
            print("Passed exams")
            self.alive = True


    def day(self):
        print(f"Glandess - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")
        print(f"Behavior - {round(self.behavior, 4)}")
        print(f"Money - {round(self.money, 3)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + "life"
        print(f"{day:^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.day()
        self.is_avive()


denis = Student("Denis")

for day in range (1, 366):
    if denis.alive == False:
        break
    denis.live(day)
