import random
try:
    people=int(input("Введите количество человек в школе:"))
    other=(random.sample(range(150, 231) ,people))
    Andrey=int(input("Введите рост Андрея(целое число): "))
except ValueError:
    print("Ошибка! Пожалуйста, введите корректное число.")
else:
    other.sort(reverse=True)
    print("Рост других в школе: ", *other)
    other.append(Andrey)
    other.sort(reverse=True)
    Andrey_number=other.index(Andrey)
    if other.count(Andrey) - 1:
        print("Рост всех после добавления Андрея: ", *other)
        print(f"Рост Андрея: {Andrey}, его номер в списке ,будет: {Andrey_number+2}")
    else:
        print(f"Рост Андрея: {Andrey}, его номер в списке ,будет: {Andrey_number + 1}")


