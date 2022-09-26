a=5
b=6
c=7
triangle=(a+b)>c #Сумма длин двух любых сторон треугольника больше длины оставшейся стороны
print(triangle)

n=2
age=str(n)
if n>=11 and n<=19:
    print("Мне",n,"лет")
elif int(age[-1::])==0:
    print("Мне",n,"лет")
elif int(age[-1::])>=5 and int(age[-1::])<=9:
    print("Мне",n,"лет")
elif int(age[-1::])==1:
    print("Мне",n,"год")
else:
    print("Мне", n, "года")