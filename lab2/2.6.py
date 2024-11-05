from colorama import init, Fore
import random
import winsound
winsound.PlaySound('C:/Users/~Darr_Kness~/PycharmProjects/pythonProject1/venv/liricheskaya-krasivaya-melodiya-2143.wav',
                   winsound.SND_FILENAME | winsound.SND_ASYNC)
def restart_game():
    try:
        secret = random.randint(1, 50)
        print(Fore.BLUE + "Хорошо, я загадал число. Попробуй его отгадать")
        i = 0
        while True:
            num = int(input("> "))
            i += 1
            if num == secret:
                print(Fore.GREEN + f"Поздравляю! Вы угадали! С {i}-ой попытки.")
                a = input("Желаете ещё раз сыграть? Введите <yes/no>: ")
                if a.lower() == "yes":
                    restart_game()
                    break
                else:
                    print("Спасибо за игру >_<")
                    exit()  # Завершение программы
            else:
                print("Нее, ты не угадал. Попробуй снова", f"Попытка номер: {i}")
                if num > secret:
                    print("Загаданное число меньше:")
                else:
                    print("Загаданное число больше:")
    except ValueError:
        print(Fore.RED + "Вы ввели не цифру. Пожалуйста, введите целое число.")
restart_game()