from colorama import init, Fore
try:
    print("В формате y = 1^2 + 2^2 + ... + n^2")
    a=int(input("Введите входные данные: "))
    sum=0
    for x in range(1,a+1):
        sum+= x**2
    print(f"Сумма квадратов от 1 до {a} равна {sum}")
except Exception as e:
    print(Fore.RED + "Неккоректно введено значение")