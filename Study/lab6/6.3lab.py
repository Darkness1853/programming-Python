# Мореплаватель Александр нашел карту с описанием местоположения пиратского клада.
# Карта представлена в виде вложенного списка, где каждый элемент- это список
# с координатами сокровища на острове
import math

# расстояния между двумя точками
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
quantity_treasure = int(input("Количество сокровищ: "))
treasure_map = []
print("Координаты сокровищ:")
for i in range(quantity_treasure):
    coordinates = input()
    x, y = map(int, coordinates.split())
    treasure_map.append((x, y))#кортеж,данные не меняются

coordinates_Andrey = input("Координаты Александра (X Y): ")
x1, y1 = map(int, coordinates_Andrey.split())

nearest_treasure = None
min_distance = float("inf")

# Поиск ближайшего сокровища
for treasure in treasure_map:
    x2, y2 = treasure
    distance = calculate_distance(x1, y1, x2, y2)
    if distance < min_distance:
        min_distance = distance
        nearest_treasure = treasure

# Вывод результата
print("Ближайшее сокровище находится на координатах:", nearest_treasure)
print("Расстояние до ближайшего сокровища:", min_distance)