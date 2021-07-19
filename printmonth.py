days = 0
ODays = 0

month = input("Enter the month ('January', ..., 'December'): ")
day = input("Enter the start day ('Monday', ..., 'Sunday'): ")

if month == "February":
    days = 28
elif month == "April" or month =="June" or month =="September" or month =="November":
    days = 30
else:
    days = 31

if day == "Monday":
    ODays = 1
elif day == "Tuesday":
    ODays = 0
elif day == "Wednesday":
    ODays = -1
elif day == "Thursday":
    ODays = -2
elif day == "Friday":
    ODays = -3
elif day =="Saturday":
    ODays = -4
elif day == "Sunday":
    ODays = -5
    
print(month)
print("Mo Tu We Th Fr Sa Su")

if -6 < ODays < 2:
    for r in range(0, 6):
        for c in range(0, 7):
            d = 7 * r + c + ODays
            if d < 1:
                print("  ", end = "")
            elif d > days:
                print("  ", end = "")
            else:
                print("{:2d}".format(d), end = "")
            if c != 6:
                print(" ", end = "")
        if r != 5:
            print("")
