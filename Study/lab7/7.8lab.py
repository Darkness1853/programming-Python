#Программа которая выводит изображение змеи по размеру поля.
# C:/Users/~Darr_Kness~/Downloads/lab10/Змейка.txt
try:
    file = input("Введите путь к файлу: ")
    size = int(input("Введите размер поля (mxm): "))
    symbol = input("Введите символ для создания тела змеи: ")

    # Создаем двумерный массив
    arr = [[' ' for _ in range(size)] for _ in range(size)]
    body=True
    # Заполняем массив
    for x in range(size):
        if x % 2 == 0:  # Четные строки
            for y in range(size):
                arr[x][y] = symbol
        else:
            # Нечетная строка
            for y in range(size):
                if body:# Тело справа
                    if y == size - 1:
                        arr[x][-1] = symbol
                    else:
                        arr[x][y] = '·'
                else:  # Тело слево
                    if y == 0:
                        arr[x][0] = symbol
                    else:
                        arr[x][y] = '·'
                body = not body
    with open(file, "w", encoding="utf-8") as text:
        for picture in arr:
            line = ''.join(picture)  #Соединяем строку в одну линию
            print(line)
            text.write(line + '\n')

    print("Программа успешно записала в файл")

except ValueError:
    print("Неправильно введен размер поля. \nВведите целое число. ")
except FileNotFoundError:
    print("Файл был ненайден")


