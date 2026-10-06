import numpy as np

# Получение размеров матрицы от пользователя
size = input("Введите размеры матрицы (например,3 4): ")
x, y = map(int, size.split())

matrix_input = []
print("Введите саму матрицу построчно:")
for i in range(x):
    row = input(f"Строка {i + 1}: ").strip().split()  # Получаем строку и разбиваем ее на элементы
    if len(row) != y:
        print(f"Ошибка: количество элементов в строке должно быть {y}. Повторите ввод.")
        exit()
    # Преобразуем элементы строки в float и добавляем в матрицу
    matrix_input.append(list(map(int, row)))

# Преобразование списка в массив NumPy
matrix = np.array(matrix_input)

# Транспонирование матрицы
matrix_T = matrix.T

# Вывод результата
print("Исходная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))  # Преобразуем элементы в строки и соединяем пробелом

print("Транспонированная матрица:")
for row in matrix_T:
    print(" ".join(map(str, row)))  # Преобразуем элементы в строки и соединяем пробелом

