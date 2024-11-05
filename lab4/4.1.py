print("Программа для разбиения входных данных в два списка.")
a=input("Введите список букв и цифр через пробел: ")
elements = a.split()
list_1=[]#список цифр
list_2=[]#список букв и символов
for i in elements:
    try:
        if float(i) or int(i):
            list_1.append(i)
    except ValueError:# в случае ошибки
        list_2.append(i)
del elements #изначальный удаляем список
print("список цифр: ","   ".join(list_1))
print("список букв и символов: ","   ".join(list_2))
#join() вывести элементы списка без скобок.