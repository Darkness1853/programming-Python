print("Программу которая создаёт аббревиатуру если в слове больше 10 символов.")
while True:
    word = input("Введите слово: ").strip()
    number = len(word) # подсчёт количества букв
    if number > 10:
        print(word[0] + str(number - 2) + word[-1])
    else:
        print(word)

    ok = input("Желаете ли вы продолжить?(да/нет)")
    if ok.lower() == "нет":
        print("До свидание!")
        exit()


