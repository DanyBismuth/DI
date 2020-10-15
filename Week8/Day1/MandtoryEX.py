# Exercise 1
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# cat1 = Cat("doudou", 2)
# cat2 = Cat("Equateur", 5)
# cat3 = Cat("Misiu", 4)
#
# # 2 Create a function that finds the oldest cat
# def oldestCat():
#   x = max(cat1.age, cat2.age, cat3.age)
#   print(f"The oldest cat is {x} years old.")
#
# oldestCat()

# Exercise 2

# class Dog:
#     def __init__(self, name_dog, height_dog):
#         self.name    = name_dog
#         self.height  = height_dog
#
#     def talk(self):
#         print("wouaf")
#
#     def jump(self):
#         jumpy = self.height * 2
#         print(f"{self.name} jump up to {jumpy} cm high")
#
#     def describe(self):
#         print("-----------------------------------------------------")
#         print(f"| Dog {self.name} : {self.height} height")
#         print("-----------------------------------------------------")
#
# davids_dog = Dog("Rex", 50)
#
# davids_dog.describe()
#
# sarahs_dog = Dog("Teacup", 20)
#
# sarahs_dog.jump()
#
# def biggestdog():
#   x = max(davids_dog.height, sarahs_dog.height)
#   if x == davids_dog.height:
#       print(f"{davids_dog.name} is the bigger dog")
#   else:
#       print(f"{sarahs_dog.name} is the bigger dog")
#
# biggestdog()

# Exercise 3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# happy_bday = Song(["Have a sunshine on you", "Happy Birthday to you !", "Have an amazing day"])
#
# print(happy_bday.sing_me_a_song())

# Exercise 4

class Zoo:
    def __init__(zoo_name, name, animals):
        self.animals = animals[]
        self.name = name

    def add_aninal(self):



