try:
    year1=int(input("BD year 1 : "))
    year2=int(input("BD year 2 : "))
    month1=int(input("BD month 1 : "))
    month2=int(input("BD month 2 : "))
    day1=int(input("BD day 1 : "))
    day2=int(input("BD day 2 : "))
    if year1<year2:
        print("Person 1 is older")
    elif year1==year2 and month1<month2:
        print("Person 1 is older")
    elif year1 == year2 and month1==month2 and day1<day2:
        print("Person 1 is older")
    else:
        print("Person 2 is older")
except ValueError:
    print("Input only numbers!")
