def main():
    numbers = []
    while True:
        list = input("Введите число (или нажмите Enter для завершения ввода): ")
        if list == "":
            break  # Завершаем ввод, если ввод пустой

        try:
            number = float(list)  # Преобразуем ввод в число с плавающей запятой
            numbers.append(number)
        except ValueError:
            print("Ошибка! Пожалуйста, введите корректное число.")

    # Проверяем, есть ли введенные числа
    if numbers:
        # Вычисляем среднее значение
        average = sum(numbers) / len(numbers)
        print(f"Среднее значение: {average}")
        #  списки чисел ниже, равные и выше среднего
        below = []
        equal = []
        above = []
        for num in numbers:
            if num < average:
                below.append(num)
        for num in numbers:
            if num == average:
                equal.append(num)
        for num in numbers:
            if num > average:
                above.append(num)
        # Печатаем результаты
        if below:
            print("Числа ниже среднего:")
            print(*below)
        if equal:
            print("Числа равные среднему:")
            print(*equal)
        if above:
            print("Числа выше среднего:")
            print(*above)
    else:
        print("Не было введено ни одного числа.")


# Запускаем программу
if __name__ == "__main__":
    main()

