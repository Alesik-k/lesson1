a=5
b=6
c=7
triangle=(a+b)>c #Сумма длин двух любых сторон треугольника больше длины оставшейся стороны
print(triangle)

n=99
y=str(n)
if int(y[-1::])==1 and y!="11":
    print("Мне",n,"год")
elif int(y[-1::])>=2 and int(y[-1::])<=4 and y!=range(12,14):
    print("Мне",n,"годa")
else:
    print("Мне",n, "лет")

n1=21
a=n1 % 10
if a==1 and a!="11":
    print("Мне",n1,"год")
elif a>=2 and a<=4 and a!=range(12,14):
    print("Мне",n1,"годa")
else:
    print("Мне",n1,"лет")