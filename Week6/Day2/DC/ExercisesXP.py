# Exercise 1
#
# my_fav_numbers = {2, 8, 91, 9, 7, 16}
# other_fav = {17, 5}
# my_fav_numbers.update(other_fav)
# my_fav_numbers.pop()
#
# friend_fav_numbers = {11, 23, 86, 55, 57}
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#
# print(our_fav_numbers)

# Exercise 2

# A tuple is a collection which is ordered and unchangeable

# Exercise 3

# Exercise 4
# for x in range(1,21):
#     print(x)

# Exercise 5

# toppings=[]
# choice=input("What do you want on your pizza!? type QUIT to stop")
#
# toppings.append(choice)
#
# while choice!= "QUIT":
#     choice = input(f"I'll add {toppings} to your pizza what else do you want ?")
#     toppings.append(choice)

#Exercise 6
#
# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
#
# tickets = []
#
# while True:
#     age = input(prompt)
#     tickets =+1
#     if age == 'quit':
#         break
#     age = int(age)
#
#     if age < 3:
#         ticket_price = 0
#     elif age < 13:
#         ticket_price = 10
#     else:
#         ticket_price = 15
#
# while age!= "quit":
#     tickets.append(ticket_price)
#
# total_price = sum(tickets)
# print(f"it will be {total_price}$")

#Exercise 7
# user = []
# age = input("How old are you ? Write stop when you are the last of group")
# age = int(age)
#
#
# while age != "stop":
#     if age > 15:
#         name = input("what is your name ?")
#         user.append(name)
#     else
#

# Exercise 8#

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0, "Apples")
#
# x = basket.count("Apples")
# print(x)
#
# basket.clear()
#
# print(basket)

# # Exercise 9
#
# list = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# for x in reversed(list):
#     print(x)

# Exercise 11

# l = []
# for i in range(3, 31):
#     if i % 3 == 0:
#         l.append(i)
#
# print(l)

#  Exercise 12

# nmbr =[]
#
# for i in range(1500, 2701):
#     if i % 5 ==0 and i % 7 == 0:
#         nmbr.append(i)
# print(nmbr)