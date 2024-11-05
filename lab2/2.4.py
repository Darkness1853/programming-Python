from colorama import init, Fore
try:
    height = int(input("Укажите высоту ёлочки: "))
    word = input("Укажите символ: ")

    for x in range(height):
        a = " " * (height - x - 1)  # количество пробелов
        b = word * (2 * x + 1)  # количество символов
        print(Fore.GREEN+a + b )
    if height >15:
        print(" "*(height-4)+word*5)
    else:
        print(" " * (height - 1) + word)
except Exception as e:
    print(Fore.RED+"Неверно введена высота")