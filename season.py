def season(a):
    if a >12:
        print(a,"out of range, please use value start if 1 to 12")
    if (a>=1) and (a<=2) or (a==12):
        print("Winter",a)
    elif (a>=3) and (a<=5):
        print("Spring", a)
    elif (a>=6) and (a<=8):
        print("Summer",a)
    elif (a>=9) and (a<=11):
        print("autumn")

season(4)