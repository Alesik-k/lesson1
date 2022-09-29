try:
    yearToday=2022
    yearBD=int(input("BD year: "))
    monthToday=9
    monthBD=int(input("BD month: "))
    dayToday=30
    dayBD=int(input("BD day: "))
    if monthBD<=monthToday:
        print("Full years as of today is :",yearToday-yearBD)
    elif monthBD==monthToday and dayBD<=dayToday:
        print("Full years as of today is :",yearToday-yearBD)
    else:
        print("Full years as of today is :",yearToday-yearBD-1)
except ValueError:
    print("Input only numbers!")