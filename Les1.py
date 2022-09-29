try:
    a = int(input("Ответ a: "))
    print(a + "29.09.2022")
except TypeError:
    print("Разные типы складывать нельзя!")
finally:
    print("Ответ принят!")

try:
    b = int(input("Введите ваш вариант ответа b "))
    import math
    print(math.sqrt(b))
except ValueError:
    print("Только положительные числа!")
finally:
    print("Ответ принят!")
