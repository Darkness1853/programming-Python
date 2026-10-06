from colorama import init, Fore
import winsound
winsound.PlaySound('C:/Users//~Darr_Kness~/PycharmProjects/pythonProject1/venv/Ludovico-Einaudi-Night.wav',
                   winsound.SND_FILENAME | winsound.SND_ASYNC) #запуск файла и асинхранизация(паралельное выполнение)

# Вывод текста
a=input(Fore.BLUE+"Ты, молодой герой, стоишь перед Сфинксом. \nОн предлагает тебе загадку:")
b=input(Fore.WHITE+'''<В пещере спрятаны сокровища, но вход охраняет страж. Чтобы попасть внутрь, тебе нужно назвать число, 
которое является суммой всех четных чисел от 2 до 100 включительно.>''')
c=input(Fore.BLUE+"Сфинкс улыбается, знаючи, что ты не сможешь вычислить это число в голове.")
d=input("Так какое это число?")
with open("C:/Users/~Darr_Kness~/PycharmProjects/pythonProject1/number.txt") as e:
    file = e.read().strip()
if str(d) == file:
    print(Fore.GREEN +f'Ответ: {d} устраивает Сфинкса и он ложиться спать,пропуская вас')
else:
    print(Fore.RED + "Вас сьедает Сфинкс")


