# Кинотеатр “Звездный” готовится к премьере долгожданного блокбастера. В зале n рядов по m мест
#  в каждом. Заказ билетов поступает онлайн, а информация о свободных местах хранится в виде
#  двумерного списка, где 1- проданный билет, а 0- свободное место.
# Поступила группа из k зрителей, которые хотят сесть рядом в одном ряду.
import random
#Зал
n=int(input("Введите количество рядов: "))#столбец
m =int(input("Введите количество мест: "))#строка
people=int(input("Введите количество человек вместе: "))
hall=[[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
count=0
for i in range(n):
    for j in range(m):
        print(hall[i][j], end=" ")
    print()

count = 0
for row in hall:
    zero_count = 0
    for seat in row:# Места в ряду
        if seat == 0:  # Если место свободно
            zero_count += 1
        else:  # Если место занято
            if zero_count >= people:
                count += 1
            zero_count = 0  # Сброс счетчика, если место занято

    # Проверка в конце строки
    if zero_count >= people:
        count += 1

if count>0:
    print(f"У нас имеется {count} свободных мест ")
else:
    print(f"К сожалению не осталось мест для {people} человек")
