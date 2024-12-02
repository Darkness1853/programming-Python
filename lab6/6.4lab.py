menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

n = len(menu)  # количество меню

while True:
    print("=" * 40)
    print("Меню")
    print("1 - Отобразить меню ресторана")
    print("2 - Найти блюдо по названию и отобразить его ингредиенты и цену.")
    print("3 - Добавить новое блюдо в меню.")
    print("4 - Изменить цену блюда")
    print("5 - Выход")
    print("=" * 40)

    v = input("Введите номер > ")

    if v == '1':
        print("Меню: ")
        for i in range(n):
            print((i + 1), menu[i][0])

    elif v == '2':
        name = input("Введите название блюда: ")
        for i in range(n):
            if menu[i][0] == name:
                print("Ингредиенты: ")
                for j in menu[i][1]:
                    print("\t", j)
                print("Цена:", menu[i][2])
                break
        else:
            print("Неверное название блюда")

    elif v == '3':
        name = input("Введите название нового блюда: ")
        for i in range(n):
            if menu[i][0] == name:
                print("Такое блюдо уже существует (придумайте новое)")
                break
        else:
            ingredients = input("Введите новые ингредиенты (через запятую): ").split(",")
            price = int(input("Введите стоимость блюда: "))
            menu.append([name, ingredients, price])
            n = len(menu)

    elif v == '4':
        name = input("Введите название блюда для изменения цены: ")
        for i in range(n):
            if menu[i][0] == name:
                new_price = int(input("Введите новую стоимость блюда: "))
                menu[i][2] = new_price  # Изменяем цену блюда
                print("Цена изменена.")
                break
        else:
            print("Такое блюдо не существует")

    elif v == '5':
        print("До свидания!")
        break
    else:
        print("Такого пункта меню нет!")