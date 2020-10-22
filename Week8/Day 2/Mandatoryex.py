# # # Exercise 1
# #
# class Family:
#
#     def __init__(self, name, age, gender, is_child):
#         self.name = name
#         self.age = age
#         self . gender = gender
#         self.is_child = False
# #
# # [ {'name':'Michael','age':35,'gender':'Male','is_child':False},
# #   {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]
# #
#
# # Exercise 2
#
# class TheIncredibles(Family):
#
#     def __init__(self, power, incredible_name):
#         self.power = power
#         self.incredible_name = incredible_name
#
#     def use_power (self, age):
#         if age >= 18:
#             print(f"{self.name} has a Super Power {self.power}")
#         else:
#             raise Exception("You have no power here !!’")
#
#     def incredible_presentation(self):
#         print(f"I'm gonna quick your ass with {self.power}, I'm {self.incredible_name}")
#
#
# flash = TheIncredibles("Flash", 9, "Male", True, "Speed", "Flash")
#
