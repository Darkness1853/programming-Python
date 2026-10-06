# Первый файл с мужскими именами "C:\Users\~Darr_Kness~\Downloads\lab10\file8.txt"
# Второй файл с женскими именами "C:\Users\~Darr_Kness~\Downloads\lab10\file7.txt"
print("Программа, которая выводит популярные имена.")
file_male = input("Введите путь к файлу с мужскими именами: ")
file_female = input("Введите путь к файлу с женскими именами: ")
gender = input("Введите пол человека (м/ж): ").lower()
quantity = int(input("Введите количество имен, которые надо вывести: "))
popularity = int(input("Вывести самые популярные имена или самые непопулярные?\n(Популярные(0)/непопулярные(1)): "))

try:
    name_scores = {}

    if gender == "м":
        with open(file_male, "r", encoding='utf-8') as text:
            for line in text:
                name, score = line.split()
                score = int(score)
                name_scores[name] = score

    elif gender == "ж":
        with open(file_female, "r", encoding='utf-8') as text:
            for line in text:
                name, score = line.split()
                score = int(score)
                name_scores[name] = score #словарь, ключи
    else:
        print("Некорректный ввод пола.")
        exit()


    def get_score(item):
        return item[1]
    # Получение пар (имя, процент популярности) из словаря
    items = name_scores.items()
    # Определение порядка сортировки (по убыванию или по возрастанию)
    reverse_order = popularity == 0
    # Сортировка имен по проценту популярности
    sorted_names = sorted(items, key=get_score, reverse=reverse_order)

    # Вывод количества имен
    if popularity == 0:
        popularity_label = 'популярных'
    else:
        popularity_label = 'непопулярных'

    print(f"{quantity} {popularity_label} имен:")
    #Срез списка, выведет столько имен, сколько ты попросил
    for name, score in sorted_names[:quantity]:
        print(f"Имя: {name}, Процент популярности: {score}")

except FileNotFoundError:
    print("Один из файлов не найден.")
except ValueError:
    print("Ошибка в формате данных файла. \nУбедитесь, что каждая строка содержит имя и процент через пробел.")

