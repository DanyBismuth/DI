# Dictionary

# Father --> Jerry
# Mother --> Beth
# cheldren --> ["Morty", "summer"]


# my_family = {"father" : "jerry", "mother" : "Beth", "children" : ["morty", "summer"]}

# dany_family = {"father":"Sauveur",
#                "mother":"Sylvie",
#                "me" : "dany",
#                "wife" : "Izabela" ,
#                "sibling" : ["Manu", "Elsa"]
#                }
# Each Flower has :
# a height
# a number
# a color
#  thorns ?

# random_flower = {
#     "height": 20,
#     "petals":4,
#     "color": "red",
#     "thorns": False,
# }

# tulip = {
#     "latin_name" : "Tulipa"
#     "height" : 50,
#     "petals" : 9,
#     "color" : 'blue',
#     "thorns" : False,
# }

# Access Data
# print(random_flower["color"])

# Modify Data
# tulip["color"]= "red"
#  tulip["shape"] = "vertical" if use a key that doesn't exist, it will create it

# # create list of dictionary
# my_flowers = [tulip, random_flower]

#
# hortensia = {
#     "latin_name" : "Hydrangea",
#     "height" : 50,
#     "petals" : 7,
#     "color" : 'blue',
#     "thorns" : False,
# }
# #
# rose = {
#     "latin_name" : "Rosa",
#     "height" : 30,
#     "petals" : 9,
#     "color" : ['red', "blue" , "white"],
#     "thorns" : True,
# }
# #
# my_flower = [rose, hortensia]
# # print("my favorite flower are")
# # print(f"{hortensia['latin_name']} is {hortensia['height']}cm high, it got {hortensia['petals']} and is {hortensia['color']} ")
#
# print("my favorite flower are")
#
# i=1
# for flower in my_flower:
#     print(f"{i})The {flower['latin_name']} is {flower['height']}cm high, it got {flower['petals']} and is {flower['color']} ")
#     i += 1

# to delete an entry
# del rose["height"]
# del can delete anything

# for item in rose:
#     print(item)
#
# for item in rose.values():
#     print(item)

# for key in rose.keys():
#     print(key, "-->" , rose[key])

# Unpacking container
# means splitting it into variable

# my_list = ["jerry", "Rick", "Morty"]
#
# father, grand_father, son = my_list
#
# print(son)

# output tuple
# for key, value in rose.items():
#     print(key, "-->", value)

# family_boys = ["jerry", "Rick", "Morty"]
# family_girls = ["beth", "???","summer"]

# for boy,girl in zip(family_boys, family_girls):
#     print(boy, "<-->", girl)

# for i, boy in enumerate(family_boys):
#     print(f"{i}) {boy}")


# products = {
#     "computer" : 1000,
#     "iphone" : 2000,
#     "Apple Wheels" : 5000,
#     "ps5" : 600,
# }
#
# # ask user how much money does he wants to spend
# # print every item that he can afford
#
# money = input("how much do you want to spend !?")
# money = int(money)
#
# for product, price in products.items():
#     if money > price :
#         print(f"you can buy {product}")
#     else:
#         print(f"too bad you cannot buy {product}")


# Exercise 2

#  Step 1 : Make a dictionnary called contacts and add three of your friend with their phone number
#  Step 2 : add another person (manually)
#  step 3 : Write a loop that print every contact with his number
#  step 4 : Write a code that searches if a given name exists in the contacts
#  Step 5 : Write a code that searches if a given number exists in the contacts, if it exist then print his name
#  Step 6 : Given another dictionnary of contacts, add it to your dictionnary
#  Step 7 : Count how many contact are in your dictionnary
#  Step 8 : Print the contacts in alphabetic order with their number

# # Step 1
#
# contacts = {
#     "rick" : "0586878399",
#     "morty" : "0543847585",
#     "summer" : "0527485982",
# }
#
# # Step 2
# contacts["beth"] = "0538888746"
#
# # step 3
# for name, phone_nb in contacts.items():
#     print(f"{name}:\t-> {phone_nb}")
#
# # Step 4
# search_name = "rick"
# found = False
# for name in contacts.keys():
#     if name.lower() == search_name.lower():
#         print(f"{name} exists in the contacts")
#
# # step 5
#
# search_nbr = "0538888746"
# found = False
#
# for name, phone_nb in contacts.items():
#     if phone_nb == search_nbr:
#         print(f"{name} is the owner of this number")
#
# # Step 6
#
# ricks_contact = {
#     "goldenfold" : "0532223344",
#     "jessica" : "0500388532",
# }
#
# contacts["goldenfold"] = "0532223344"
# contacts["jessica"] = "0500388532"
#
# for name, phone_nb in ricks_contact.items(): OR contacts.update(ricks_contacts)
#     contacts[name]= phone_nb
#
# # Step 7
# nb_of_contacts = len(contacts.key())
# print(f"There are {nb_of_contacts} contacts")
#
# # Step 8
#
# sorted_contacts = sorted(contacts.keys())
# for contact in sorted_contacts:
#     print(f"{contact}\t -> {contacts[contact]}")


# Comprehension

# name = ["pedro", "jack", "rick", "Morty"]
#
#
# magician_names = []
# for name in names:
#     magician_name = "the Great " + name
#     magician_names.append(magician_name)
#
# # As a list comprehension
#
#  magician_names = ["The Great "+name for name in names]
#
#  # For Dictionaries
#
# persons_age ={
#     "rick": 57,
#     "pedro": 44,
#     "Mario" : 5,
#     "luigi": 45,
#
# }
#
# persons_age_next_year = {person:age+1 for person, age in persons_age.item()}

# Exercise

products_wallmart = {
    "Computer": 1000,
    "Iphone": 2000,
    "Apple Wheels": 5000,
    "PS5": 600
}
products_amazon = {
    "Samsung Galaxy": 800,
    "Computer": 1500,
    "Apple Wheels": 3000,
    "XBox": 600,
}

# print only the products that exists in both dictionaries, and the lowest prices

for product in products_wallmart.keys():
    if product in products_amazon.keys:
        lowest_price = min(products_wallmart[product], products_amazon[product])

        print(f"")
