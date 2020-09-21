your_password=input("Please give me your password")

if len(your_password)== 10:
    print("the first letter is:",your_password[0])
    print("the last  letter is:",your_password[-1])

    print(your_password[0])
    print(your_password[0:1])
    print(your_password[0:2])
    print(your_password[0:3])
    print(your_password[0:4])
    print(your_password[0:5])
    print(your_password[0:6])
    print(your_password[0:7])
    print(your_password[0:8])
    print(your_password[0:9])
    print(your_password[0:10])

    jumbled_pwd =  your_password[2] + your_password[1] + your_password[3] + your_password [5] + your_password [4]

else:
    print("sorry, your password needs to be 10 characters long")
