# Class Attribute

# class Phone:
#
#     spanish_name ="telefono"
#     objs_count =0
#
#     def __init__(self, brand, size, adapter_type):
#         self.brand = brand
#         self.size = size
#         self.adapter_type = adapter_type
#
#
#         Phone.objs_count += 1
#         if Phone.objs_count % 100 == 0:
#             Phone.anniversary()
#     @classmethod
#     # This wil tell python the fonction should receive the class itself and not the instance
#     def anniversary(cls):
#         print(f"Happy BD to phone Class !! {cls.objs_count} phones have been created so far")
#
# phone = Phone("Apple", 10,"Apple Adapter")
#
# print(Phone.spanish_name)
# phone.anniversary()

# class Animal():
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def drink(self):
#         print(f"{self.name} is drinking")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
#
# class Cat(Animal):
#
#     def growl(self):
#         print("meow")
#
#
# class Dog(Animal):
#
#     def growl(self):
#         print("Woaf")
#
#
# dog = Dog("Fox")
#
# dog.sleep()

# Child fonction overwrite parent's fonction
# First Child Function then parents


# First step: Create a Hero class (representing a hero in a war game)
# The attributes:
# - current_life_points
# - max_life_points
# - hit_dammage
# - energy
# - name
# - level
# - xp
# - is_alive (True unless his life points go below 0, a dead hero can't do anything)
# The methods:
# - level_up() --> increase max_life_points by 2 and set current_life_points to maximum
# - hit(hero_obj) --> decrease the other hero's life points by hit_dammage, gain 10 XP, if he
#   reaches 100 XP, he levels up
# - die()
# Second step: Create three specialized heros
# -> A Wizard
# -> A Warrior
# -> A LuckyGuy
# They are also heroes, they can do everything a hero can do, but
# When taking a hit, the wizard reflects it and he hits his ennemy with the half of the power
# When he hits the Warrior hit dammage is multiplied by 2
# When the lucky guy levels up, he actually takes two levels
class Hero:
    def __init__(self, name):
        """
        Hero class representing a warrior character
        :param name: (str) Name of the character
        """
        self.name = name
        self.level                  = 1
        self.max_energy             = 100
        self.max_life_points        = 100
        self.hit_dammage            = 10
        self.xp                     = 0
        self.is_alive               = True
        self.current_energy         = self.max_energy
        self.current_life_points    = self.max_life_points

    def describe(self):
        print("="*50)
        print(f"Hero {self.name}")
        if self.is_alive:
            print(f"Life: {self.current_life_points}/{self.max_life_points}")
            print(f"Energy: {self.current_energy}/{self.max_energy}")
            print(f"XP: {self.xp}")
            print(f"Dammage: {self.hit_dammage}")
        else:
            print("Dead.")
        print("="*50)

    def hit(self, other_hero):
        """
        Hits another hero
        :param hero: (Hero) Hero to hit
        """
        print(f"{self.name} hit {other_hero.name} !")
        other_hero.takes_hit(self.hit_dammage, self)
        self.get_xp(10)

    def get_xp(self, xp_amount):
        """
        Increase XP points
        Level up if the XP reaches 100
        :param xp_amount: (int) Amount of xp to add
        """
        self.xp += xp_amount
        if self.xp >= 100:
            self.level_up()

    def takes_hit(self, dammage, ennemy_hitting):
        """
        Taking dammage
        Kills the hero if current_life_points goes below 0
        :param dammage: (int) Dammage amount to take
        """
        print("Ouch !")
        self.current_life_points -= dammage
        if self.current_life_points <= 0:
            self.die()

    def die(self):
        """
        Kills the hero
        """
        self.is_alive = False

    def level_up(self):
        """
        Levels up the hero
        Add 2 to max_life_points
        Give him all his life points back
        Increment level and set xp back to 0
        """ # Docstring
        self.max_life_points += 2
        self.current_life_points = self.max_life_points
        self.level += 1
        self.xp = 0


class Wizard(Hero):
    def takes_hit(self, dammage, ennemy_hitting):
        """
        Taking dammage
        Reflects half of the dammage to the ennemy
        Kills the hero if current_life_points goes below 0
        :param dammage: (int) Dammage amount to take
        """
        super().takes_hit(dammage, ennemy_hitting)
        if self.is_alive:
            ennemy_hitting.takes_hit(dammage // 2, self)


class Warrior(Hero):
    def __init__(self, name):
        """
        Hero class representing a warrior character
        :param name: (str) Name of the character
        """
      super().__init__(name)
    self.hit_dammage *= 2

class LuckyGuy(Hero):

    def level_up(self):
        """
        Levels up the hero
        Add 2 to max_life_points
        Give him all his life points back
        Increment level and set xp back to 0
        """ # Docstring

        super().level_up()
        super().level_up()

my_hero     = Hero("Rick")
my_wizard   = Wizard("Morty")
my_hero.describe()
my_wizard.describe()
my_hero.hit(my_wizard)
my_hero.describe()
my_wizard.describe()






