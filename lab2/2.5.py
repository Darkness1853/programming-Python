from colorama import init, Fore
try:
    a=float(input("Введите год собаки: "))
    if a < 0:
        print("Ошибка!")
    elif a <= 1:
        s = 10.5
        print(s)
    elif a <= 2:
        s = 10.5 * 2
        print(s)
    else:  # a > 2
        s = 10.5 * 2 + (a - 2) * 4
        print(s)
except Exception as e:
    print(Fore.RED + "Неверно введён год")