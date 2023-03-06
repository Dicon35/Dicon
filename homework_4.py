class Human:
    height = 180
    satiety = 180



class Son(Human):
    satiety = 20



class GrandSon(Human):
    satiety = 80


nick = Son()
denis = GrandSon()

print(nick.satiety)
print(denis.satiety)