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


class Secret:
    public_field = "this is public"
    _private_field = "avoid using this please"
    __real_field = "I am hiden"


s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_field)