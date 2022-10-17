# Совершенные числа - найти все совершенные числа до chisla1
chislo1=int(input("Enter your number: "))
for i in range(1,chislo1+1):
    summ=0
    for j in range(1,i):
        if i%j==0:
            summ+=j
    if i==summ:
        print((str(i)+ " совершенное число"))