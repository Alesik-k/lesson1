a=int(input("Enter a three-digit number: "))
if 99<a<1000:
    y=str(a)
    print(int(y[:1:1])+int(y[1:2:1])+int(y[2:3:1]))
    print(int(y[:1:1])*int(y[1:2:1])*int(y[2:3:1]))
else:
    print("The number isn't correct")


