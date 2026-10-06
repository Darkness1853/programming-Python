import random

print("Если первое слово больще второго по размеру,то пишеться любое из чисел,если второе слово больше первого,то обрезаем второе слово.")
a=input("Введите первое слово: ")
b=input("Введите второе слово: ")
l1=len(a)
l2=len(b)
if (l1==0)or(l2==0)or(l1==l2==0):
    print("Ошибка! Некорректное количество слов")
else:
    if l1>l2:
        s=random.randint(1,2)
        if s==1:
            print(a)
        else:
            print(b)
    elif l1==l2:
        print(f"Оба числа одинаковы:\n{a}\n{b}")
    else:
        cut =b[:2]
        print(cut)
