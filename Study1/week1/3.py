# A2
"""У вас есть робот, который умеет резать слова. Он делит каждое слово на две части и
меняет их местами. Например, слово “робот” превратится в “отроб”. Вам нужно написать
программу, которая будет реализовывать этот реверс-алгоритм.
"""
# def swap():
#     while True:
#         text = input("Введите текст: ")
#         first_char = ""
#         second_char = ""

#         if 2 < len(text) <= 100:
#             half = len(text) // 2
#             for i,char in enumerate(text):
#                 if i < half:
#                     first_char += char
#                 else:
#                     second_char += char
#             print(second_char + first_char)
#             break
#         else:
#             print("Введите длину строки от 3-100")
    
    
# def main():
#     swap()

# if __name__ == "__main__":
#     main()

# A3
'''Создаётся система, которая анализирует сообщения из двух слов. Для проверки важна
длина слов. Если первое слово короче второго, то второе слово должно быть обрезанно до
длины первого слова. Это необходимо для анализа. Например, если введено “кот слон”, то
“слон” обрезается до “сло”. Еслиже дилина первого слова больше или равна, то выведите
случайное из этих этих слов.'''

# from random import randint
# def equal():
#     while True:
#         try:
#             a,b = map(str, input("Программа уравнит слова.\nВведите 2 слова.\n").split())
#             if len(a) < len(b):
#                 print(b[:len(a)])
#             elif a > b:
#                 print(a[:len(b)])
#             else:
#                 cnt = randint(0, 1)
#                 print(a) if cnt == 0 else print(b)
            
#         except ValueError:
#             print("Ошибка! Некорректное количество слов")
# def main():
#     equal()

# if __name__ == "__main__":
#     main()

# A4
"""Дан список слов. Требуется создать новый список, в котором удалены все дубликаты, но
порядок первых вхождений слов сохранён"""

# def unique():
#     unique_word = []
#     words = input().split()
#     for word in words:
#         if word not in unique_word:
#             unique_word.append(word)
#     print(" ".join(unique_word))

# def main():
#     unique()

# if __name__ == "__main__":
#     main()

# A

"""В волшебной стране “Перевертыши” все фразы пишутся в обратном порядке. Вам нужно
написать программу, которая поможет перевести фразу с обычного языка на “перевертышный”. Для этого нужно разделить фразу на два слова и поменять их местами. Например,
“фразу перевернуть” превратится в “перевернуть фразу”.
"""

# def swap():
#     while True:
#         try:
#             a,b = map(str, input("Введите два слова, они будут в обратном порядке: ").split())
#             print(b + " " + a)
#             break
#         except ValueError:
#             print("Ошибка! Некорректное количество слов")


# def main():
#     swap()

# if __name__ == "__main__":
#     main()

# B

"""Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем предложении такая допущена. Необходимо исправить каждый такой повтор. Повтор это –
слово , ТОЛЬКО один пробел, и снова то же слово.
"""

# def correct_text():
#     while True:
#         text = input("Введите текст с повторяющими подряд словами: ").split()
#         data = ""
#         final_text = []
#         for word in text:
#             if word not in data:
#                 final_text.append(word)
#                 data = word
#             else:
#                 continue
#         print(" ".join(final_text))
#         break

# def main():
#     correct_text()

# if __name__ == "__main__":
#     main()

# C
"""Вы – разработчик программы для обработки текстовых сообщений в мессенджере. Ваша
задача – написать программу, которая форматирует сообщения, вставляя символ точки
между каждыми двумя соседними символами. В этой задаче можно использовать цикл,
но можно обойтись и без него (нужно догадаться самому). Программа должна корректно работать с различными типами входных строк, включая пустые и строки из одного
символа"""

# def join():
#     text = input("Введите строку:")
#     print(".".join(text))

# def main():
#     join()

# if __name__ == "__main__":
#     main()

# D
"""Хайку – жанр традиционной японской лирической поэзии века, известный с XIV века.
Оригинальное японское хайку состоит из 17 слогов, составляющих один столбец иероглифов. Особыми разделительными словами – кирэдзи – текст хайку делится на части из 5,
7 и снова 5 слогов. При переводе хайку на западные языки традиционно вместо разделительного слова использую разрыв строки и, таким образом, хайку записываются как
трёхстишия"""

# def haiky():
#     while True:
#         inputs = []
#         rules = []
#         vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
#         cnt = 0
#         print("Введите 3 строки для проверки текста на Хайку")
#         for _ in range(3):
#             value = input()
#             inputs.append(value)

#         for text in inputs:
#             for char in text:
#                 if char in vowels:
#                     cnt += 1
#             rules.append(cnt)
#             cnt = 0

#         if rules == [5, 7, 5]:
#             print("Хайку!")
#         else:
#             print("Не хайку.")
#         break

# def main():
#     haiky()

# if __name__ == "__main__":
#     main()

# E
"""Секретное агентство «Super-Secret-no» решило для шифрования переписки своих сотрудников использовать «метод бутерброда». Сначала буквы слова нумеруются:
первая буква получает номер 1,
последняя буква - номер 2,
вторая – номер 3,
предпоследняя –номер 4, потом третья . . . и так для всех букв. Затем все буквы записываются в шифр в порядке своих номеров и в конец зашифрованного слова добавляется
#, который нельзя использовать в сообщениях. """

# def encoder():
#     while True:
#         try:
#             encoder_text = input("Введите слово для зашифровки: ")
#             result = ""
#             left = 0
#             right = len(encoder_text) - 1
#             while left <= right:
#                 if left < right:
#                     result += encoder_text[left] + encoder_text[right]
#                 else:
#                     result += encoder_text[left]
#                 left += 1
#                 right -= 1
#             print(result+"#\n")
#             break

#         except Exception as e:
#             print(f"Ошибка: {e}")

# def decoder():
#     while True:
#         try:
#             decoder_text = input("Введите слово для расшифровки: ")
#             if "#" not in decoder_text :
#                 print("Введите шифр с # в конце\n")
#                 continue
#             else:
#                 a = decoder_text[:-1] # убираем #
#                 decoded = ""
#                 decoded += a[0::2] + a[1::2][::-1]
#                 print(decoded)
#                 break

#         except Exception as e:
#             print(f"Ошибка: {e}")

# def main():
#     while True:
#         try:
#             print("Метод бутерброда.\n")
#             choose = int(input("Введите число\n1 - зашифровать\n2 - расшифровать\n3 - выйти\n"))
#             if choose == 1:
#                 encoder()
#             elif choose == 2:
#                 decoder()
#             else:
#                 break
#         except ValueError:
#             print("Введите корректные данные\n")

# if __name__ == "__main__":
#     main()

# F
"""Вы работаете над созданием новой системы управления паролями для небольшой компании. Вам нужно написать программу, которая будет генерировать пароли определённой
сложности и длины по запросу пользователя. Программа должна учитывать различные
критерии сложности пароля, предоставляя пользователю выбор, какие символы должны
быть включены в пароль."""

# def ask_info():
#     print("Программа сгенерирует вам пароль под критерии\nВведите данные: \n")
#     while True:
#         try:
#             ask_len = int(input("желаемая длина пароля (целое число): "))
#             ask_big = str(input("\nнужны ли заглавные буквы (да/нет): ").strip().lower())
#             ask_small = str(input("\nнужны ли строчные буквы (да/нет): ").strip().lower())
#             ask_num = str(input("\nнужны ли цифры (да/нет): ").strip().lower())
#             ask_special = str(input("\nнужны ли специальные символы (да/нет): ").strip().lower())
#             return ask_len,ask_big,ask_small,ask_num,ask_special
#         except Exception:
#             print(f"Введите правильные типы данных\n")
        

# def create_password(ask_len,ask_big,ask_small,ask_num,ask_special):
#     from random import choice
#     import string

#     char = ""
#     result = ""

#     if ask_big == "да":
#         char += string.ascii_uppercase
#     if ask_small == "да":
#         char += string.ascii_lowercase
#     if ask_num == "да":
#         char += string.digits
#     if ask_special == "да":
#         char += "!@#$%^&*()_-+=<>?/|"
#     if len(result) == 0:
#         result = "Не из чего генерировать\n"
#     else:
#         while ask_len > len(result):
#             result += choice(char)

#     return result

# def main():
#     result = ask_info()
#     ask_len,ask_big,ask_small,ask_num,ask_special = result
#     password = create_password(ask_len,ask_big,ask_small,ask_num,ask_special)
#     print(password)

# if __name__ == "__main__":
#     main()

# G
"""Вы – разработчик программного обеспечения для спортивных новостных сайтов. Вам поручено написать программу, которая автоматически определяет победителя матча по результатам, выведенным на табло стадиона."""

# def comp_match():
#     while True:
#         try:
#             print("Программа посчитает какая команда выиграла\n" \
#             "Введите данные в формате команда-команда счет:счет\n")
#             text = input().strip()
#             if text.count("-") > 1 or text.count(":") > 1:
#                 print("вы ошиблись с количеством - и :\n")
#                 continue
#             teams, score = text.rsplit(" ", maxsplit=1)
#             first_team, second_team = teams.split("-")
#             first_score, second_score = score.split(":")
#             if first_score > second_score:
#                 print(first_team)
#             elif first_score < second_score:
#                 print(second_team)
#             else:
#                 print("Ничья")
#             break
#         except Exception as e:
#             print(f"Ошибка: {e}")


# def main():
#     comp_match()

# if __name__ == "__main__":
#     main()