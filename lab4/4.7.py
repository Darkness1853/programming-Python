print("""Программа для вычисления контрольной цифры 
пластиковой карты с помощью алгоритма Луна""")
try:
    number = input("Введите номер банковской карты: ").strip()
    num_str = str(number) # Приводим к строке
    sum_even = 0   # сумма четных
    sum_odd = 0    # сумма нечетных
    # Перебираем цифры, начиная с конца
    for x in range(len(num_str)):
        digit = int(num_str[len(num_str) - 1 - x])  # считываем цифры с конца
        if x % 2 == 0:  # нечетные позиции с конца
            sum_odd += digit
        else:  # четные позиции с конца
            even_numbers = digit * 2
            if even_numbers > 9:
                even_numbers -= 9
            sum_even += even_numbers
    total_sum = sum_even + sum_odd
    # Проверка по контрольной цифре
    if total_sum % 10 == 0:
        print("Корректный номер")
    else:
        print("Некорректный номер")
except ValueError:
    print("Некорректный номер")