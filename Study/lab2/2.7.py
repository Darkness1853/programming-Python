from colorama import init, Fore
try:
    ticket = input("Введите шестизначный номер билета: ")  # Считываем номер как строку
    if len(ticket) == 6 and ticket.isdigit():  # Проверка длины и на целые цифры
        if sum([int(ticket[0]), int(ticket[1]), int(ticket[2])]) == sum([int(ticket[3]), int(ticket[4]), int(ticket[5])]):
            print(Fore.YELLOW + "Вы счастливчик! Ваш билет - счастливый")
        else:
            print("К сожалению, вам попался обычный билет")
    else:
        print("Некорректный билет. Билет должен содержать 6 цифр.")
except Exception as e:
    print(Fore.RED + "Произошла ошибка")