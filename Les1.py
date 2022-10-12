# Вывести на экран столько элементов ряда Фибоначчи (рядом чисел, в котором каждое
# последующее число является суммой двух предыдущих), сколько указал пользователь.
n=int(input("Enter your number fobonachchi: "))
f_n_2=f_n_1=1
print(f_n_1,f_n_2, end=" ")
for i in range(2,n):
    fn=f_n_2+f_n_1
    f_n_2=f_n_1
    f_n_1=fn
    print(fn, end=" ")

print()
#factorial
a=int(input("Enter your number for factorial: "))
i=1
factorial=1
while i<=a:
     factorial*=i
     i+=1
print("Facrotial for", a, "is", factorial)