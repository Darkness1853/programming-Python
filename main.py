
import time
import sys
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Печатает один символ
        sys.stdout.flush()       # Обновляет вывод
        time.sleep(delay)        # Задержка перед выводом следующего символа
    print()  # Переход на новую строку после вывода всего текста

# Использование функции
slow_print(Fore.GREEN + "В какую пещеру вы войдете?", delay=0.1)