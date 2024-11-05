a=input("Введите слова: ")
s=a.count(" ")
if s%2!=0:
    words = a.split()
    if len(words) >= 2:
        words[0], words[1] = words[1], words[0]
        result = ' '.join(words)
        print("Строка после замены слов:", result)
    else:
        print("Недостаточно слов для замены.")
else:
    print("Ошибка! Некорректное количество слов \nКоличество слов нечетное, местами можно поменять только при четном количестве слов.")



