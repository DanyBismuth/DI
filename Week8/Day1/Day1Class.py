# Class (blue print for how a think should look like) no _ on the name made like Hashtag no space

# class Dog():
#
#     def __init__(self, age, name, race):
#         # print('a dog is created')
#         self.age = age
#         self.name = name
#         self.race = race
#
#         self.energy_level = 100
#         self.distanceran = 0
#
#     def bark(self):
#         print(f"{self.name} is Barking ! Woof")
#
#     def eat(self):
#         print(f"{self.name} is eating nothing")
#         self.energy_level += 30
#
#         if self.energy_level > 100 :
#             self.energy_level = 100
#
#     def run(self):
#         if self.energy_level < 40:
#             print(f"{self.name} is tired, he cannot run right now")
#         else:
#             print(f"{self.name} is running")
#             self.energy_level -= 15
#             self.distanceran += 3
#             print(f"{self.name} ran {self.distanceran}km")
#
#     def describe(self):
#         print("-----------------------------------------------------")
#         print(f"| Dog {self.name} : {self.age} years old {self.race}")
#         print(f"| Energy : {self.energy_level} /100")
#         print(f"| Travelled : {self.distanceran} km")
#         print("-----------------------------------------------------")
#
# my_dog = Dog(age = 0, name = "Fox", race ="bulldog")
# my_dog2 = Dog(2, "swiffer", "pitbull")

# Dog.bark(my_dog)
# Same as :
# my_dog.bark()
# my_dog2.eat()
# my_dog2.run()
# my_dog2.run()
# my_dog2.eat()
# my_dog2.run()
# my_dog2.run()
# my_dog2.eat()
# my_dog2.run()
# my_dog2.run()
# my_dog2.run()
# my_dog2.run()
# my_dog2.eat()

# my_dog2.describe()


# Exercise Spell Book
# you need to create a class that represents a Spell
#  a Spell has  :
# a name
# an invocation sentence
# an action

#  create a class that represent a Spell book
#  a spell book has a list of spell and three methods :
# add spell : Add a spell to the book
# remove spell : Remove a spell to the book
# use spell  Says the invocation sentence of the Spell

class Spell():

    def __init__(self, name, invocation, action, min_level):
        self.name       = name
        self.invocation = invocation
        self.action     = action

        self.min_level = min_level


my_spell1 = Spell("Flamethrower", "embrasetoi", "set on fire", 4)
my_spell2 = Spell("bubble", "bubububble", " throw bubble of shampoo", 2)
my_spell3 = Spell("poisongaz", "HSSSSSS", "the atmosphere is not breathable", 6)


class SpellBook():

    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def remove_spell(self, spell):
        self.spells.remove(spell)

    def describe(self):

        print("-----------------------------------------------------")
        print(f"| Here are the spell")
        for spell in self.spells:
            print("-", spell.name)
        print("-----------------------------------------------------")


# Creat a "Wizard" Class
# Name
# Level (from 1)
# a spells book

class Wizard():

    def __init__(self, name, wizard_name):
        self.name = "name"
        self.wizard_name = wizard_name

        self.level = 1
        self.book = SpellBook

