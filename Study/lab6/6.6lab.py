import numpy as np

# Получение размера матрицы от пользователя
n = int(input("Введите размер квадратной матрицы: "))

# Создание квадратной матрицы
matrix_input = []
print("Введите саму матрицу построчно:")
for i in range(n):
    row = input(f"Строка {i + 1}: ").strip().split()
    if len(row) != n:
        print(f"Ошибка: количество элементов в строке должно быть {n}. Повторите ввод.")
        exit()
    matrix_input.append(list(map(int, row)))  # Добавляем строку в матрицу, преобразуя элементы в int

# Преобразование списка в массив NumPy
matrix = np.array(matrix_input)

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))

# Меняем местами угловые элементы
matrix[0, n-1], matrix[0, 0], matrix[n-1, 0], matrix[n-1, n-1] = \
    matrix[n-1, n-1], matrix[n-1, 0], matrix[0, 0], matrix[0, n-1]

# Вывод измененной матрицы
print("Матрица после замены угловых элементов:")
for row in matrix:
    print(" ".join(map(str, row)))