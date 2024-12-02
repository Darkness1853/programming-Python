#C:/Users/~Darr_Kness~/Downloads/lab10/file5.txt Первый файл
#C:/Users/~Darr_Kness~/Downloads/lab10/file6.txt Второй файл
print("Программа ищёт слово в двух файлах")
a = input("Введите путь к первому файлу: ")
b = input("Введите путь ко второму файлу: ")
word = input("Введите слово, которое вы ищете: ")
find_word = False
find_word2 = False
try:
    # Ищем слово в первом файле
    with open(a, "r") as file_1:
        for line in file_1:
            if word in line:
                find_word = True
                break
    if find_word:
        print(f"В первом файле есть слово {word}")
    else:
        print(f"В первом файле нет слова {word}")
    # Ищем слово во втором файле
    with open(b, "r") as file_2:
        for line in file_2:
            if word in line:
                find_word2 = True
                break
    if find_word2:
        print(f"Во втором файле есть слово {word}")
    else:
        print(f"Во втором файле нет слова {word}")
    if not find_word and not find_word2:
        print(f"К сожалению, слово {word} не было найдено.")
except FileNotFoundError:
    print("Один из файлов не найден.")
except ValueError:
    print("Ошибка преобразования данных.")


