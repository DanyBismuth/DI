# # To define a list use []
#
# my_list = [1, 2, 3]
#
# my_names=["rick", "morty", "Summer"]
#
# My_favorite_letters_numbers = ["a",2,"letter b", 599]
#
# print(my_names[0:2])
#
# dany_list = ["Papa", "Maman", "Dany", "Manu", "Elsa"]
#
# # like the strings
#
# print(len(dany_list))
#
# dany_list.append("Roger")
# dany_list.remove("Maman")
# dany_list.pop(2)
#
# print(dany_list)
#
# # while Loops
#
# your_password=input("Please give me your password")
#
# if len(your_password)== 10:
#     print("the first letter is:",your_password[0])
#     print("the last  letter is:",your_password[-1])
#
#     i=1
#     while i<= 10:
#         print(your_password[0:i])
#         i = i +1
#
# else:
#     print("sorry, your password needs to be 10 characters long")

# Exercise :

# Ask user for toppings on his pizza, and add them to a list until he says "STOP"

# toppings=[]
# choice=input("What do you want on your pizza!? type STOP to stop")
#
# toppings.append(choice)
#
# while choice!= "STOP":
#     choice = input(f"I'll add {toppings} to your pizza what else do you want ?")
#     toppings.append(choice)
#
# print(toppings)

# Exercise 2

# Ask the user for a password, the pwd need to match :
# should have 6 Characters minimum and 12 max
# If the password do not match the criteria, display a message and ask him again

# Bonus: user only has 3 chance to put the right one if not kick him out

# user_password=input("Password please ? between 6-12 characters")
# # print(len(user_password))
#
# attempt = 2
# while 0 < attempt < 4:
#
#     if 6<len(user_password)<12:
#         print("good to go")
#     else:
#         input(f"try again you have {attempt} attempt left")
#         attempt = attempt - 1


# Exercise 3

# movie theater charges different ticket prices depending on a person's age.
# If a person is under age of 3, the ticket is free;
# If they are between 3-12, the ticket is $10, and if they are over 12 the ticket is 15$

# Write a loop in which you ask users their age (until user writes STOP), and then tell them the cost of their movie ticket.


# The break keyword

# while 1==1:
#     user_name=input("what's your name ?")
#     if user_password == "stop":
#         break

# the use of a flag

# toppings=[]
# choice=""
#
# stop_the_loop =False
#
# while not stop_the_loop:
#     choice=input("give me a topping:")
#     toppings.append(choice)
#
#     if len(toppings)>3 :
#         stop_the_loop=True
#
#     if choice=="ananas":
#         stop_the_loop = True

# For Loops

# smith_family=["rick", "morty", "summer", "beth", "jerry"]
#
# # for member in Sequence
#
# for member in smith_family:
#     print("hello", member)
#
# print("I'm out of the loop")

# Exercise
# create a list of family members
# ask them one by one how old they are
# If they are below 16, remove them from the list

smith_family = ["rick", "morty", "summer", "beth", "jerry"]

for member in smith_family:
    age=input(f"{member}, how old are you?")
    age=int(age)
    if age<16:
        smith_family.remove(member)

print(smith_family)



