# Напишите программу, которая будет открывать файл со списком слов, случайным образом выби
# рать два из них и сцеплять вместе для получения итогового пароля. При создании пароля исходите
#  из следующего требования: он должен состоять минимум из восьми символов и максимум из деся
# ти, каждое из используемых слов должно быть длиной хотя бы в три буквы. Кроме того, сделайте
#  заглавными первые буквы обоих слов, чтобы легко можно было понять, где заканчивается одно и
#  начинается другое. По завершении процесса полученный пароль должен быть отображен на экране.
# C:/Users/~Darr_Kness~/Downloads/lab10/text10.txt
from colorama import Fore,Style
import random
print("Программа которая создает пароли, соединяет два слова в файле \nРазмер пароля от 8-10")
try:
    file = input("Введите путь к файлу: ")
    len_words=int(input("Введите количество паролей: "))
    with open(file,"r",encoding="utf-8") as text:
        words_list=[]
        for line in text:
            words = line.split()
            for word in words:
                if len(word)>=3:
                    words_list.append(word)
        passwords=[]
        if len(words_list)<2:
            print("В файле недостаточно слов.")
            exit()
        else:
            for _ in range(len_words):
                while True:
                    #title()-поднимает регистр
                    word1=random.choice(words_list).title()
                    word2 = random.choice(words_list).title()
                    password=word1+word2
                    if 8 <=len(password)<=10:
                        passwords.append(password)
                        break
            if len(passwords)>0:
                print("Результат: ")
                for x in passwords:
                    print(x)
            else:
                print("В данном файле не найдены подходящие слова для создания пароля.")
                exit()
except FileNotFoundError:
    print("Файл был не найден, проверьте правильность введённого пути.")
except ValueError:
    print("Ошибка,введите целое число.")


