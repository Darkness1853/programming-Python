def encrypt(text):
    n = len(text)
    encrypted = []
    # Создание списка номеров
    e = []
    for i in range(n):
        if i % 2 == 0:  # Чётные индексы
            e.append(text[i // 2])  # Первая, третья и т.д.
        else:  # Нечётные индексы
            e.append(text[n - (i // 2) - 1])  # Вторая, четвёртая и т.д.

    # Объединяем в строку и добавляем символ #
    encrypted_text = ''.join(e) + '#'

    return encrypted_text

def decrypt(encrypted_text):
    encrypted_text = encrypted_text.rstrip('#')  # Удаляем символ #
    n = len(encrypted_text)
    d = [''] * n

    for i in range(n):
        if i % 2 == 0:  # Чётные индексы
            d[i // 2] = encrypted_text[i]  # Размещаем в 1, 3, 5...
        else:  # Нечётные индексы
            d[n - (i // 2) - 1] = encrypted_text[i]  # В 2, 4, 6...

    return ''.join(d)

# Ввод выбора пользователя
a = input("Введите цифру: 0 - зашифровать или 1 - расшифровать: ")

if a == '0':  # Зашифровать
    message = input("Введите сообщение для шифрования: ")
    encrypted_message = encrypt(message)
    print("Зашифрованное сообщение:", encrypted_message)

elif a == '1':  # Расшифровать
    message = input("Введите зашифрованное сообщение: ")
    decrypted_message = decrypt(message)  # здесь исправлено использование переменной
    print("Расшифрованное сообщение:", decrypted_message)
else:
    print("Введённые данные неправильные")

