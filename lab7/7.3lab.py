# C:/Users/~Darr_Kness~/Downloads/lab10/file6.txt
print("Программа которая вычисляет процент буквы")
file = input("Введите путь к файлу: ")
word_index = input("Учитывать только верхний регистр? (да/нет): ")
word = input("Введите букву: ")

# Проверяем, учитывается ли регистр
if word_index.lower() == "да":
    pass
else:
    word = word.lower()

miss = int(input("Введите точность измерений: "))

if len(word) != 1 or not word.isalpha():
    print("Пожалуйста, введите одну букву.")
else:
    total_words = 0
    cnt = 0
    try:
        with open(file, "r") as text:
            for line in text:
                # Разделяем строку на слова, убирая знаки препинания
                words = line.split()
                total_words += len(words)  # Количество слов в строке
                if word_index.lower() == "да":
                    for word_list in words:
                        if word in word_list:  #
                            cnt += 1
                else:
                    for word_list in words:
                        if word.lower() in word_list.lower():
                            cnt += 1
        if total_words == 0:
            print("Файл пустой или не содержит слов")
        else:
            percentage_words = (cnt / total_words) * 100
            print(f"Процент слов с буквой '{word}': {percentage_words:.{miss}f}")
    except FileNotFoundError:
        print("Один из файлов не найден.")
    except ValueError:
        print("Ошибка преобразования данных.")