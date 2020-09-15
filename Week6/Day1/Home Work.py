#Write a program that checks the validity of a password.
#
#Ask the user for a password, and then make sure that the password follow those criterias:
#
#At least 1 letter.
#Minimum length of password: 6. (Check on google how to find the length of a string)
#Maximum length of password: 12.
# Bonus
#At least 1 upper case letter.
#At least 1 lower case letter.

your_password=input("please enter your password ! with at least one upper and lower case letter / 6 to 12 letters ")Dany

if len(your_password)<6:
    print("The password must be greater than 6 characters")
elif len(your_password)>12:
    print("The password must be less than  characters")
else:
    print("Welcome")
