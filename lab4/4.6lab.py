import time
from colorama import init, Fore
import random
question=input("Желаете ли вы сыграть в орёл и орешку?(да/нет)")
if question.lower()=="да":
    def random_coin():
        count = 0# количество бросков монеты
        last_coin = "" #результат последнего броска
        streak = 0#количество идущих подряд
        while streak <3:
            count +=1
            coin=random.randint(0,1)
            if coin==0:
                print(Fore.YELLOW +"О", end=' ')
                current_coin = "О"
                time.sleep(1)
            else:
                print(Fore.YELLOW +"Р", end=' ')
                current_coin = "Р"
                time.sleep(1)
            if last_coin == current_coin:
                streak += 1
            else:
                streak = 1
            last_coin = current_coin
        print(f"\nКоличество попыток: {count}")
    random_coin()
else:
    print("Попробуйте в следующий раз.")


