#Найдите его наибольшую цифру в числе
n=input("Enter your number 1: ")
a=0
for i in n:
    if int(i)>int(a):
        a=i
print(a)

#Сформируйте из введённого числа обратное по порядку входящих в него цифр и выведите на экран.
y=input("Enter your number 2: ")
print(y[::-1])