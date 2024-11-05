# import random
# team1=input("Введите спортивную команду 1: ")
# team2=input("Введите спортивную команду 2: ")
# time1 = random.randint(0, 10)  # значение от 0 до 10 для первой команды
# time2 = random.randint(0, 10)  # значение от 0 до 10 для второй команды
# print(f"{team1} - {team2} {time1}:{time2}")
# if time1>time2:
#     print(f"Выиграла команда{team1}")
# elif time1 == time2:
#     print(f"Ничья")
# else:
#     print(f"Выиграла команда{team2}")

result = input("Введите результат матча (например: Команда1-Команда2 5:3): ")
# Проверка, что символы "-" и ":" встречаются ровно по одному разу
if result.count("-") == 1 and result.count(":") == 1:
    # Делим строку на части: команды и счёт
    teams, score_part = result.split(" ")  # разделяем по пробелу
    # Разделяем команды по "-"
    team1, team2 = teams.split("-")
    # Разделяем счёт по ":"
    time1p, time2p = score_part.split(":")
    try:
        # Преобразуем строки с результатами в целые числа
        time1 = int(time1p)
        time2 = int(time2p)

        # Выводим результат матча
        print(f"{team1} - {team2} {time1}:{time2}")

        # Определяем победителя
        if time1 > time2:
            print(f"Выиграла команда {team1}")
        elif time1 < time2:
            print(f"Выиграла команда {team2}")
        else:
            print("Ничья!")
    except ValueError:
        print("Ошибка: Счёт должен быть целым числом.")
else:
    print("Ошибка: неверный формат ввода. Убедитесь, что формат команды: 'Команда1-Команда2 A:B'")
