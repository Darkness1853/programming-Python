# В данном задании вам предлагается реализовать простейший вариант игры "Морской бой". Дано
#  поле 4х4 и 4 однопалубных корабля, которые расставлены рандомно. Пользователю каждый раз
#  показывается поле
import random
from colorama import Fore,Style
print("-" * 40)
print("*"*15+"Морской бой"+"*"*14)
print("-" * 40)

while True:
    try:
        size = int(input("Введите размер поля (mxm): "))
        ship = int(input("Введите количество однопалубных кораблей: "))
        bomb = int(input("Введите количество бомб на поле: "))
    except ValueError:
        a=input(Fore.RED+"Ошибка, введите целое число.\nЖелаете остаться или все-таки уйти?(да/нет)")
        print(Style.RESET_ALL)
        if a.lower() != "да":
            print("Спасибо за то, что сыграли в игру.")
            exit()
        else:
            continue

    if size * size < (ship + bomb):
        b=input(Fore.RED+"Ошибка, количеств бомб и кораблей больше размера игрового поля.\nЖелаете остаться или все-таки уйти?(да/нет)")
        print(Style.RESET_ALL)
        if b.lower() != "да":
            print("Спасибо за то, что сыграли в игру.")
            exit()
        else:
            continue

    size_game = [["·"] * size for _ in range(size)]
    cnt = 0
    move = 0
    code = input("Введите специальный код:")
    if code == "12345":
        print(Fore.YELLOW+"Код сработал.")
        print(Style.RESET_ALL)
        # Установка бомб
        for _ in range(bomb):
            while True:
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
                if size_game[x][y] == "·":  # проверка место свободно
                    size_game[x][y] = "B"
                    break

        # Установка кораблей
        for _ in range(ship):
            while True:
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
                if size_game[x][y] == "·":  # Проверка место свободно
                    size_game[x][y] = "S"
                    break
    else:
        print("Код не сработал.")
        bomb_locations = []  # Список для хранения координат бомб
        for _ in range(bomb):
            while True:
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
                if (x, y) not in bomb_locations:
                    bomb_locations.append((x, y))
                    break

        # Установка кораблей
        ship_locations = []  # Список для хранения координат кораблей
        for _ in range(ship):
            while True:
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
                if (x, y) not in ship_locations and (x, y) not in bomb_locations:
                    ship_locations.append((x, y))
                    break


    # Игра
    while True:
        for row in size_game:
            print(" ".join(row))  # вывод поля

        try:
            fire = input("Введите координаты (x,y): ")
            x, y = map(int, fire.split(","))
            if size_game[x][y] == "B":
                print(Fore.RED+f"Вы проиграли\nКоличество пораженных кораблей: {cnt}\nПотрачено ходов: {move}")
                print(Style.RESET_ALL)

                break
            elif size_game[x][y] == "S":
                print(Fore.YELLOW+"Вы попали по кораблю.")
                print(Style.RESET_ALL)
                cnt += 1
                size_game[x][y] = "X"
            else:
                print("Промах")
            move += 1

            # Победа
            if cnt == ship:
                print(Fore.YELLOW+f"Вы выиграли! Количество ходов: {move}")
                break

        except (ValueError, IndexError):
            print(Fore.RED+"Ошибка ввода. Убедитесь, что вы ввели координаты в формате x,y\n и они находятся в пределах поля.")
            print(Style.RESET_ALL)

    # Повтор
    restart = input("Желаете ещё раз сыграть в игру?(нет/да): ")
    if restart.lower() != "да":
        print("Спасибо за то, что сыграли в игру.")
        break

