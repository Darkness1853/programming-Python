def count_vowels(line):
    vowels = 'аоэеиыуёюя'  # Гласные русского алфавита можно использовать char
    count = 0  # счётчик гласных
    # Перебираем каждый символ в строке
    for i in line:
        if i.lower() in vowels:  # преобразует в нижний регистр lower(),Если символ - гласная
            count += 1  # Увеличиваем счётчик
    return count  # Возвращаем количество гласных

a=input("Введите три строки хайку (/-начало новой строки):")
lines =a.split("/")
# Проверяем количество строк
if len(lines) != 3:
    print("Не хайку. Должно быть 3 строки.")  # Если строк не три
else:
    # Подсчитываем гласные в каждой строке
    counts = []
    for line in lines:
        counts.append(count_vowels(line))  # Добавляем количество гласных в список

    # Проверяем соответствие чисел 5, 7 и 5
    if counts == [5, 7, 5]:
        print("Хайку!")  # Если соответствует
    else:
        print("Не хайку.")  # Если не соответствует
