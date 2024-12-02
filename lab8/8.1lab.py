# На старых мобильных телефонах текстовые сообщения набирались при помощи цифровых кнопок.
#  При этом одна кнопка ассоциируется сразу с несколькими буквами, а выбор зависел от количества
#  нажатий на кнопку.
# 4433555555666110966677755531111
dictionary = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}
def enter_number(number_press):
    result = ""
    cnt = 0
    current_number = ""

    for char in number_press:
        if char == current_number:
            cnt += 1
        else:
            if current_number:
                symbols = dictionary.get(current_number)
                if symbols:
                    # Обработка нажатий
                    index = (cnt - 1) % len(symbols)  # Индекс в зависимости от нажатий
                    if len(result) == 0 or result[-1] == ' ':
                        result += symbols[index].upper()
                    else:
                        result += symbols[index].lower()  # Заглавная ставиться, если первое слово или после пробела

            current_number = char  # Запоминаем текущую цифру
            cnt = 1  # Сбрасываем счётчик нажатий

    # Обработка последнего нажатия
    if current_number:
        symbols = dictionary.get(current_number)
        if symbols:
            index = (cnt - 1) % len(symbols)
            if len(result) == 0 or result[-1] == ' ':
                result += symbols[index].upper()
            else:
                result += symbols[index].lower()

    return result


# Ввод пользователем
number_press = input("Введите список цифр: ")
exit_number = enter_number(number_press)
print("Результат:", exit_number)