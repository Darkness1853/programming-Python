from colorama import init, Fore
import time
import random
import winsound
winsound.PlaySound('C:/Users/~Darr_Kness~/PycharmProjects/pythonProject1/venv/liricheskaya-krasivaya-melodiya-2143.wav',
                   winsound.SND_FILENAME | winsound.SND_ASYNC)
a=input("Желаете ли вы испытать удачу?(да/нет)")
if a.lower()=="да":
    lucky_ticket = [random.randint(1, 49) for _ in range(6)]
    player_ticket = [random.randint(1, 49) for _ in range(6)]
    lucky_ticket = " ".join(map(str, lucky_ticket))  # с помощью map преобразуем каждое значение
    player_ticket = " ".join(map(str, player_ticket))  # в списке из числа в строку, без этого .join()не будет работать
    print(f"Вам выпал билет с номером: [{player_ticket}]")
    time.sleep(2)
    if player_ticket == lucky_ticket:
        print(Fore.YELLOW + "Поздравляю,вы выиграли главный приз!")
    else:
        print("Не расстраивайтесь, в следующий раз повезёт!")
        print(Fore.WHITE + f"Номер счастливого билета: [{lucky_ticket}]")
else:
    print("Попробуйте в следующий раз!\n (ﾉω･､)")