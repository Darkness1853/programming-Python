# Магический квадрат — это квадратная таблица, заполненная различными целыми числами так,
# что сумма чисел в каждой строке, каждом столбце и на обеих диагоналях одинакова.
# Для магических квадратов размерности 3x3, чтобы достичь такой симметрии,
# эквивалентно нужно, чтобы все числа от 1 до 9 были расставлены в квадрате.
from random import choice
def check_magic_square(matrix):
    sum1=sum(matrix[0])#сумма первой строки
    for x in matrix:#проверка суммы 3 строк
        if sum(x)!=sum1:
            return False
    for y in range(3):#Сумма 3 столбцов,проверка
        if sum(matrix[i][y] for i in range(3)) !=sum1:
            return False
    #проверка диоганалей
    if sum(matrix[i][i] for i in range(3)) !=sum1:
        return False
    if sum(matrix[i][2-i] for i in range(3)) !=sum1:
        return False
    return True

def random_magic_square():#заполняем магический квадрат
    while True:
        m = []
        for i in range(3):
            m.append([0] * 3)
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3):
            for j in range(3):
                m[i][j] = choice(number)
                number.remove(m[i][j])
        if check_magic_square(m):
            return m

# Генерация магического квадрата
magic_square = random_magic_square()
# вывод матрицы на экран
for i in range(3):
    for j in range(3):
        print(magic_square[i][j], end=" ")
    print()
