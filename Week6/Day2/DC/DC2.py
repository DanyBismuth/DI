birthday = input("Can I please have your birthday date DD/MM/YYYY")
bd_d = birthday[:2]
bd_m = birthday[4:-5]
bd_y = birthday[-4:]

bd_d = int(bd_d)
bd_m = int(bd_m)
bd_y = int(bd_y)

from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")

d1_d = d1[:2]
d1_m = d1[3:-5]
d1_y = d1[-4:]

d1_d = int(d1_d)
d1_m = int(d1_m)
d1_y = int(d1_y)

age = d1_y - bd_y
the_m = d1_m - bd_m
the_d = d1_d - bd_d

candle = 0


if (the_d == 0) & (the_m == 0) & age>=10:

    candle = str(age)[-1:]
    candle = int(candle)

    candle_line = "i"*candle

    print(f"___{candle_line}___")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

elif (the_d == 0) & (the_m == 0) & age<10:
    candle_line = "i"*age

    print(f"___{candle_line}___")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

else:
    print("it is not your birthday >u<")