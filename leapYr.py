year = int(input("Enter year: "))
if (year % 4 == 0):
    if (year%100 == 0):
        if (year % 400 == 0):
            print("Leap")
        else:
            print("Non Leap")
    else:
        print("Leap")
else:
    print("Non leap")
