# A
'''Вам дана строка, состоящая из латинских букв и цифр. Удалите из нее все цифры, оставив
только буквы.
Входные данные
Строка
Выходные данные
Для каждой строки выведите ту же строку, но без цифр.'''

# def main():

#     word = str(input('Введите строку состоящую из букв и цифр: '))
#     result = ""
#     if word.isalpha() == True:
#         print(f'Строка состоит только из букв: : {word}')
#         exit()

#     for i in word:
#         if i.isalpha():
#             result += i

#     print(result)

# if __name__ == "__main__":
#     main()

# B
'''Робот Чаппи был назначен ответственным за генерацию паролей для всех аккаунтов планеты Омикрон Персей 8. Но Чаппи — известный жадина, и он считает, что тратить лишние
символы на пароли — это расточительство!
Поэтому он придумал гениальную идею: если в пароле какой-то символ повторяется,
нужно оставить его только один раз.
Помогите Чаппи сэкономить символы. Напишите программу, которая убирает все повторяющиеся символы из пароля, оставляя только первое вхождение каждого символа.
'''

# def main():
#     while True:

#         print("Программа выводит лишь неповторяющие символы из пароля\nВведите 'q' для выхода из программы.\n")
#         password = input().strip()
#         temp = ''
#         result = ''
#         if password == 'q':
#             exit()
#         for i in password:
#             if i not in temp:
#                 temp = i
#                 result += i
#         break

#     print(result)

# if __name__ == "__main__":
#     main()

# C

"""Напишите программу, которая рисует ёлку заданной высоты с помощью символа #. Высота ёлки вводится с клавиатуры.
Входные данные
Высота елки
Выходные данные
Елка высоты n
Пример: n = 5
"""

# def main():
#     try:
#         print("Введите первое число - символ, второе число - высота елки")
#         symbol = input().strip()
#         size = int(input().strip())
#     except ValueError:
#         print("Введите первое число - символ, второе число - высота елки")

#     for i in range(size):
#         space = " " * (size - i - 1)
#         leaves = symbol[0] * (2 * i + 1)
#         print(space + leaves)

#     print(" " * (size - 1) + symbol[0])
# if __name__ == "__main__":
#     main()

# D
"""Даны две строки: text и word. Напишите функцию, которая проверяет, можно ли составить
слово word из букв строки text, используя буквы в порядке их следования в text, но не
обязательно подряд.
Входные данные
Две строки
Выходные данные
True, если слово можно составить, и False в противном случае
"""

# def main():
#     try:
#         text, word = map(str, input("Программа проверяет можно ли составить слово из букв.\nВведите две строки в формате N N:   ").split())
#     except ValueError:
#         print("Введите две строки в формате N N")

#     letters = list(text)

#     for letter in word:
#         if letter in letters:
#             letters.remove(letter)
#         else:
#             print("False")
#             exit()

#     print("True")

# if __name__ == "__main__":
#     main()

# E

"""Компьютер загадывает число от 1 до 100. Пользователь пытается угадать его. После каждой попытки программа сообщает, является ли загаданное число большим или меньшим
по сравнению с введённым. Игра продолжается до тех пор, пока число не будет угадано.
"""

# from random import randint

# def game():
#     secret_number = randint(1, 100)

#     print("Программа будет загадывать число, ваша роль угадать его.\n")

#     while True:
#             try:
#                 number = int(input("Введите число от 1 до 100: "))
    
#                 if number > secret_number:
#                     print("Загаданное число меньше")
#                 elif number < secret_number:
#                     print("Загаданное число больше")
#                 else:
#                     print(f"Вы угадали число!!!\nЗагаданное число {secret_number}")
#                     break
#             except ValueError:
#                  print("Введите число от 1 до 100")

# def main():
#     game()

# if __name__ == "__main__":
#     main()

# F

# def change():
#     print("Введите целое число, которое кратно 10:")
#     while True:
#         try:
#             amount = int(input())

#             if amount % 10 !=0:
#                 print("Целое число не кратно 10, введи кратное")
#             else:
#                 change = amount
#                 count = 0
#                 print(f"Введенная сумма равна {change}\n")
#                 if change >= 1000:
#                     num1000 = change // 1000
#                     count += num1000
#                     change = change - (num1000 * 1000)
#                     print(f"1000 - {num1000}")
#                 if change >= 500:
#                     num500 = change // 500
#                     count += num500
#                     change = change - (num500 * 500)
#                     print(f"500 - {num500}")
#                 if change >= 100:
#                     num100 = change // 100
#                     count += num100
#                     change = change - (num100 * 100)
#                     print(f"100 - {num100}")
#                 if change >= 50:
#                     num50 = change // 50
#                     count += num50
#                     change = change - (num50 * 50)
#                     print(f"50 - {num50}")
#                 if change >= 10:
#                     num10 = change // 10
#                     count += num10
#                     change = change - (num10 * 10)
#                     print(f"10 - {num10}")
#                 print(f"Всего купюр: {count}")
#                 break
#         except ValueError:
#             print("Введенное значение неправильное.")
    
# def main():
#     change()

# if __name__ == "__main__":
#     main()

# F

# def change(money):
#     nominal = [1000,500,100,50,10]
#     count = 0

#     for nom in nominal:
#         if money >= nom:
#             banknote = money // nom
#             count += banknote
#             money = money - (banknote * nom)
#             print(f"{nom} - {banknote}")
#     print(f"Всего купюр: {count}")

    

# def main():
#     print("Введите число кратное 10: ")
#     while True:
#         try:
#             money = int(input())
#             if money <= 0 or money % 10:
#                 print("Число должно быть положительным и кратным 10.")
#             else:
#                 change(money)
#                 break
#         except ValueError:
#             print("Ошибка, введите целое число")

# if __name__ == "__main__":
#     main()

# G

# from random import randint

# def info():
#     print("""Инструкция "Камень-ножницы-бумага\nПользователь может вводить:\n
# ’камень’ или ’stone’ или ’к’ или ’st’\n
# ’ножницы’ или ’scissors’ или ’н’ или ’sc’\n
# ’бумага’ или ’paper’ или ’б’ или ’p’\n""")

# def create_dict():
#     steps = {}
#     groups = [
#         (["камень","stone","к","st"], 1),
#         (["ножницы","scissors","н","sc"], 2),
#         (["бумага","paper","б","p"], 3)
#     ]

#     for keys, value in groups:
#         for key in keys:
#             steps[key] = value

#     return steps

# def run_game(steps):

#     count = [0, 0]
#     while True:
#         try:
#             key = input("Введите: ")
#             if key in steps:
#                 user_step = steps[key]
#                 bot_step = randint(1, 3)

#                 if (user_step == 1 and bot_step == 2) or \
#                     (user_step == 2 and bot_step == 3) or \
#                     (user_step == 3 and bot_step == 1):
#                     count[0] += 1
#                     print(f"Выиграл\nСчет: {count[0]} : {count[1]}")
#                 elif (user_step == bot_step):
#                     print(f"Ничья\nСчет: {count[0]} : {count[1]}")
#                 else:
#                     count[1] += 1
#                     print(f"Проиграл\nСчет: {count[0]} : {count[1]}")

#                 if count[0] == 3 or count[1] == 3:
#                     print(f"Игра окончена\nСчет: {count[0]} : {count[1]}")
#                     break
#             else:
#                 info()

#         except ValueError:
#             print("Введите верные данные")
#             info()

# def main():
#     info()
#     steps = create_dict()
#     run_game(steps)

# if __name__ == "__main__":
#     main()

# H

# def count(text): # подсчет символов, букв, цифр, пробелов, знаков препинания
#     try:
#         len_str = len(text)
#         len_alpha = sum(1 for char in text if char.isalpha())
#         len_num = sum(1 for char in text if char.isdigit())
#         len_space = sum(1 for char in text if char.isspace())
#         len_punct_marks = sum(1 for char in text if not char.isspace() and not char.isdigit() and not char.isalpha())
#     except ValueError:
#         print("Ошибка в логике работы")
#     return len_str,len_alpha,len_num,len_space,len_punct_marks

# def register(text): # преобразование строк
#     first_alpha_big = text.capitalize()
#     list_lowel = "аеёиоуыэюя"
#     replace_text = first_alpha_big
#     for char in list_lowel:
#         replace_text = replace_text.replace(char, "*")
#     return first_alpha_big, replace_text

# def search_switch(text): # поиск количество встречаемых подстрок, замена вхождений.
#     user_text = input("Введите подстроку для поиска в тексте: ")
#     user_text2 = input("Введите слово для замены в тексте: ")
#     count = 0
#     start = 0
#     while True:
#         pos = text.find(user_text, start)
#         if pos == -1:
#             break
#         count += 1
#         start = pos + 1
#     print(f"Найдено {count} вхождений подстроки {user_text}\nТекст перед заменой: {text}\nПосле:{text.replace(user_text, user_text2)}")

# def analiz(text): # проверка слов в строке, поиск самого длинного слова
#     count = 0
#     big_word = ""
#     temp = ""
#     for word in text:
#         temp += word
#         if word == " ":
#             count += 1
#             if len(big_word) < len(temp):
#                 big_word = temp
#             temp = ""
#     print(f"Слов в строке: {count}\nСамое длинное слово: {big_word}")

# def check(text): # проверка состоит ли строка только из цифр / букв, начинается ли строка с заглавной буквы, заканчивается ли строка знаком препинания
#     check_only_num = text.isdigit()
#     check_only_alpha = text.isalpha()
#     check_first_big = text[0].isupper()
#     check_last_punct = text[-1] in ".,!?;:"
#     return check_only_num, check_only_alpha, check_first_big, check_last_punct

# def form(text): # оформление
#     len_str,len_alpha,len_num,len_space,len_punct_marks = count(text)
#     first_alpha_big, replace_text = register(text)
#     check_only_num, check_only_alpha, check_first_big, check_last_punct = check(text)
#     print(f"Длина строки: {len_str}\nКоличество букв: {len_alpha}\nКоличество цифр: {len_num}\nКоличество пробелов: {len_space}\nКоличество знаков препинания: {len_punct_marks}\nПреобразованная строка: {first_alpha_big}\nСтрока после замены гласных на *: {replace_text}\nПроверка состоит ли строка только из цифр: {check_only_num}\nПроверка состоит ли строка только из букв: {check_only_alpha}\nПроверка начинается ли строка с заглавной буквы: {check_first_big}\nПроверка заканчивается ли строка знаком препинания: {check_last_punct}")
#     search_switch(text)
#     analiz(text)

# def run():
#     while True:
#         print("""Данная программа проверяет, преобразовывает, подсчитывает текст.\n
#         Введите текст, предложение в одну строку: \nДля выхода из программы введите 'q'""")
#         text = input()
#         if text.lower() == "q":
#             print("Выход из программы")
#             break
#         if len(text) == 0:
#             print("Вы ничего не ввели")
#         else:
#             form(text)

    

# def main():
#     run()

# if __name__ == "__main__":
#     main()

# J

def deencoder(text, step, choose):
    encoder_text = ""
    punc = "!?._- "
    if choose == 2:
        step = -step
    for char in text:
        if char in punc:
            encoder_text += char
            continue
        else:
            encoder_text += chr(ord(char) + step)
    return encoder_text

def run_caesar():
    while True:
        try:
            print("Программа, которая реализовывает шифратор и дешифратор по методу Цезаря.")
            choose = int(input("Введите число.\n1 - зашифровать\n2 - расшифровать\n3 - выйти\n"))
            if choose < 3 and choose > 0:
                text = input(f"Введите текст чтобы {"зашифровать" if choose == 1 else "расшифровать"}\n")
                step = int(input("Введите число - смещение\n"))
                result = deencoder(text, step, choose)
                print(result)
            elif choose == 3:
                break
            else:
                print("Введите 1,2,3\n")
        except ValueError:
            print("Неправильно введены данные")
        except KeyboardInterrupt:
            print("Досвидание!")
            break
def main():
    run_caesar()

if __name__ == "__main__":
    main()
