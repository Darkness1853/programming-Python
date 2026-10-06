def func(x):
    return x ** 2 / (10 + x ** 3)

a = -2 #границы
b = 5
n = 10000 #разбиение на 10000
h = (b - a) / n#ширина интервала
sum= 0.5 *(func(a)+func(b)) #площадь одной трапеции
for i in range(1,n):#суммирование средних столбцов
    x=a+i*h
    sum+=func(x)
interval=sum*h
print(f"{interval:.10f}")