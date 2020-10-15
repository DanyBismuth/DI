# Exercise (easy)
# Write a program that counts the number of element for a list, without the len function.

# name=['Alex','Mike','Dylan','Yossi']
#
# counter = 0
# for i in name :
#     counter = counter +1
# print(str(counter))

# exercise (easy)
# Write a program that print every name that starts by 'a'

# name=['Alex','Mike','Dylan','yossi','Alan']
#
# for i in name:
#     if i.startswith("A"):
#         print(i)

# Exercise (easy) To talk with
# Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.

# for i in range(1, 11) :
#     if (i== 3 | i==6):
#         continue
#
#     print(i)
#
# Exercise (easy)
# Use a for loop to print the numbers from 1 to 20, inclusive.

# Printing inclusive range
# start = 1
# stop  = 20
# step  = 1
# stop +=step #now stop is 20
#
# for i in range(start, stop, step):
#     print(i, end=', ')


# Exercise (easy)

# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
#
# millions= range(1,1000001)
# for million in millions:
#     print(million)


# Exercise (easy)
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers .


# millions= range(1,1000001)
# for million in millions:
#     print(million)

# Exercise (easy)
# Write a program that returns the index of the first occurrence of an item in a list.


# Exercise (easy)
# Write a little program that concatenate two lists together without using the + sign.
# Exercise (medium)
# Create a board as following by using for loops:
#     X
#     XX
#     XXX
#     XXXX
#     XXXXX
#     XXXXXX
#     XXXXX
#     XXXX
#     XXX
#     XX
#     X
# Exercise (medium)
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
# Exercise (medium)
# Write a program that insert an item at a defined index.
# Exercise (medium)
# Take a list of popular car manufacturers
# Paste it into your code, and store it in a variable.
# Convert it into a list using Python (don’t do it by hand!)
# Print out a message saying how many manufacturers/companies are in the list
# Print the list of manufacturers in reverse/descending order (Z-A)
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them
# Print the above information out with meaningful output messages.
# (Bonus: There are a few duplicates in the list:
# Remove these programmatically. (Hint: you can use sets to help you)
# Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, ...”), and also print out a message saying how many companies are now in the list).
# (Bonus: print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name)
# Exercise (medium)
# You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.
# current_players = ['Mario', 'Luigi', 'Peach']
# new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
# At the end of your program, print(current_players) should be:
# ['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']
# Exercise (medium)
# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****
# Exercise (medium)
# What is the output of the following?¶
#     x = ['ab', 'cd']
#     for i in x:
#         i.upper()
#     print(x)
# Exercise (medium)
# What is the output of the following?¶
#     x = ['ab', 'cd']
#     for i in x:
#         x.append(i.upper())
#     print(x)
# Exercise (hard)
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
# Exercise (easy)
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# Exercise (hard)
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
# Exercise (hard)
# Draw the following pattern using for loops:
#       *
#      ***
#     *****
# 8:02
# Exercise (hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if my_list[j] < my_list[minimum]:
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)
# Exercise (hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 13, 34, 23, 12, 111]
# for fillslot in range(len(arr)-1,0,-1):
#     max_pos = 0
#     for location in range(1, fillslot+1):
#         if arr[location] > arr[max_pos]:
#             max_pos = location
#     tmp = arr[fillslot]
#     arr[fillslot] = arr[max_pos]
#     arr[max_pos] = tmp
# Exercise (hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_str = "I do"
# my_text = "What I can't build, I do not understand."
# found   = False
# index = 0
# for letter in my_text:
#     if letter == my_str[index]:
#         index += 1
#         if index == len(my_str):
#             found = True
#             break
#     else:
#         index = 0
# if found:
#     print("<{}> was found in the text !".format(my_str))
# else:
#     print("<{}> is not in the text".format(my_str))
# Exercise (hard)
# Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# Exercise (hard)
# Write a program that put each word of a string in a list without using the split function.
# Exercise (hard)
# Write a program that prints the longest word in a list.
# Exercise (hard)
# 8:02
# On while loops:
# Exercise (easy)
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza .
# Exercise (easy)
# A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 .
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
# Exercise (easy)
# Given a list, use a while loop to print out every elements from the end to the beginning.
# Exercise (easy)
# Without your computer, guess the output of this piece of code:
# i = 1
# while True:
#     if i == 3:
#         break
#     print(i)
#     i + = 1
# Exercise (easy)
# Use a while loop to print every number from 5 to 100
# Exercise (easy)
# What is the purpose of this program:
# user_input = input("> ")
# while user_input != "p4ssw0rd":
#     print("Access denied.")
#     user_input = input("> ")
# print("Access granted!")
# Exercise (easy)
# What is the problem in this program:
# user_input = input("Password: ")
# while user_input != "my_password":
#     print("Access denied")
# print("Access granted")
# And how can you fix it ?
# Exercise (medium)
# Take the last exercise, and apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.
# Exercise (medium)
# Given a list, use a while loop to print out every element which his index is even.
# Exercise (medium)
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which can see the movie.
# Try to add the allowed ones to a list.
# Exercise (medium)
# This time you have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.
# Exercise (medium)
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.
# Exercise (medium)
# Count the number of spaces in a string.
# Exercise (medium)
# Count the number of words in a string.
# Exercise (medium)
# Write a program that calculate the number of upper case letters and lower case letters in a string.
# Exercise (medium)
# Without your computer, guess the output of this program:
# index = 0
# my_list = [321, 312, 123, 434, 1235]
# while index < len(my_list):
#     s = str(my_list[index])
#     print(s[-1])
#     index += 1
# Exercise (medium)
# What is the output of the following?¶
#     x = "abcdef"
#     i = "a"
#     while i in x:
#         x = x[:-1]
#         print(i, end = " ")
# Exercise (medium)
# You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.
# current_players = ['Mario', 'Luigi', 'Peach']
# new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
# At the end of your program, print(current_players) should be:
# ['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']
# 8:02
# Exercise (hard)
# Convert a string into password format Example: input : "mypassword" output: "***********"
# Exercise (hard)
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.
# Exercise (hard)
# Using the list sandwich_orders from Exercise 8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
# Exercise (hard)
# Encrypt and decrypt a string with Caesar cipher.
# Check on internet to understand how Caesar cipher works.
# Exercise (hard)
# Create a python mastermind, make a program that asks the user for a string, and then generate a sequence of random letters (the length of the sequence should be the same as the user's string) until he falls on the user's string. At each iteration, the program can compare his random string to the user's string, and keep the right letters.