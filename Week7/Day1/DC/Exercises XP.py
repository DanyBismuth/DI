# # Exercise 1
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# number = zip(keys, values)
# dict = set(number)
# print(dict)
#
# # Exercise 2
#
# store = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": ["France -> blue", "Spain -> red", "US -> pink", "green",]
# }
#
# store["number_stores"] = 2
#
# print("Zara's clients are young, price-conscious, and highly sensitive to the latest fashion trends.")
#
# store["country_creation"]="Spain"
#
# def set_key(dictionary, key, value):
#      if key not in dictionary:
#          dictionary[key] = value
#      elif type(dictionary[key]) == list:
#          dictionary[key].append(value)
#      else:
#          dictionary[key] = [dictionary[key], value]
#
# set_key(store, "international_competitors", "Desigual")
#
# del store["creation_date"]
#
# print(store["international_competitors"][-1:])
#
# print(f"the major color by country are :{store['major_color']}")
#
# print(len(store))
#
# print(store.keys())
#
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
#
#
# def merge(store, more_on_zara):
#     res = {**store, **more_on_zara}
#     return res
#
# zara = merge(store, more_on_zara)
# print(zara)
#
# print(store["number_stores"])


# Exercise 3

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

enum_user = enumerate(users)
print(list(enum_user))
