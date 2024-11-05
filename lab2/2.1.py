from colorama import init, Fore
try:
    print(Fore.BLUE+"Нахождение самого высокого и низкого человека")
    people = int(input("Введите количество человек: "))
    heights = []
    if people >= 2:
            for i in range(people):
                height = int(input(f"Введите рост человека {i + 1} (введите 0 для завершения ввода): "))

                if height > 0:
                    heights.append(height)  # Добавляем только положительные значения
                elif height == 0:
                    break  # Завершаем ввод при значении 0
                else:
                    print("Рост не может быть отрицательным.")

            # Проверяем, достаточно ли введённых ростов для сравнения
            if len(heights) < 2:
                print("Некого сравнивать.")
            else:
                max_height = max(heights)
                min_height = min(heights)

                print(Fore.WHITE+f"Самый высокий человек с ростом: {max_height}")
                print(Fore.WHITE+f"Самый маленький человек с ростом: {min_height}")
    else:
        print("Мало людей")
except Exception as e:
    print(Fore.RED+"Произошла ошибка программы,проверьте верно ли введены цифры")
