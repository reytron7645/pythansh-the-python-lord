year=int(input('ENTER A YEAR : '))
if (year % 400 == 0):
    print("This is a leap year")
elif (year % 4 ==0):
    print("This is a leap year")
else:
    print("This year is not a leap year")