a = input("Введите список чисел: ")
elements = list(map(int, a.split()))
#a.split() на отдельные строки
#map() приминяет заданную функцию к каждому элементу
#list() преобразует в строку
list_1 = []
for x in range(1,len(elements)):#сравнение начинается с второго элемента
    if elements[x] > elements[x - 1]:
        list_1.append(elements[x])
print("Выходные данные: ",*list_1)