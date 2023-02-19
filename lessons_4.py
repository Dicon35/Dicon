# class Human:
#     height = 160
#     satiety = 180
#
#
#
# class Student(Human):
#     satiety = 10
#
#
#
# class Worker(Human):
#     satiety = 50
#
#
# nick = Student()
# denis = Worker()
#
# print(nick.satiety)
# print(denis.satiety)
#
# class Grandparent:
#     height = 170
#     satiety = 50
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
#
# class Child(Parent):
#     height = 130
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self. age)
#
#
# child = Child()
#
#
# class Secret:
#     public_field = "this is public"
#     _private_field = "avoid using this please"
#     __real_field = "I am hiden"
#
#
# s = Secret()
# print(s.public_field)
# print(s._private_field)
# print(s._Secret__real_field)
#
#
# class Hello:
#     hello = "Hello"
#     _hello = "Hello"



# class Hello:
#     def __init__(self):
#         print("Hello")
#
# class Hello_Wolrd(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World")
#
#

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# c = Class2()

# class Grandparent:
#     def about(self):
#         print("I am Grandparent")
#
#     def about_myself(self):
#         print("I am grandparent")
#
# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")

class Computer:
    def __init__(self):
        self.memory = 128


class Display:
    def __init__(self):
        self.screen = "4k"

class SmartPhone(Display, Computer):
    def print(self):
        print(self.screen)
        print(self.memory)

iphone = SmartPhone()
iphone.print()
