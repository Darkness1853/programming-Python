a=input("Если хотите перевести из двоичной в десятичную,то напишите 1:\nЕсли хотите перевести из десятичной в двоичную,напишите 0:\n")
if a ==1:
    bin = input("Введите двоичное число: ")
    decimal_number = 0
    degree = 0

    # Цикл по двоичному числу от последнего к первому
    for i in range(len(bin) - 1, -1, -1):
        if bin[i] == "1":
            decimal_number += 2 ** degree
        degree += 1

    print(f"Десятичное число: {decimal_number}")
else:
    decimal_number = int(input("Введите десятичное число: "))
    b = []
    while decimal_number > 0:
        b.append(decimal_number % 2) #получение остатка от деления
        decimal_number //= 2 # целочисленное
    b.reverse() #избавляемся от скобок и запятых
    for i in b:
        print(i, end="")




