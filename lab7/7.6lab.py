# C:/Users/~Darr_Kness~/Downloads/lab10/file6.txt
def encrypt(text): # Шифрование
    return text[::-1]
def decrypt(text):# Дешифрование
    return text[::-1]

print("Программа, которая считывает файл и зашифровывает/дешифрует файл.")
file = input("Введите путь к файлу: ")

cryptographer = input("Дешифровать (0) или шифровать сообщение (1)\nВыбери вариант (0/1): ")

try:
    with open(file, "r", encoding='utf-8') as text:
        my_list = text.readlines()

    # Объединяем строки в один текст
    text_1 = ''.join(my_list)

    if cryptographer == "1":  # Шифровать
        encrypted_text = encrypt(text_1)
        with open(file, "w", encoding='utf-8') as text:
            text.write(encrypted_text)
            print("Программа успешно выполнена")
        print("Зашифрованное сообщение:")
        print(encrypted_text)
    elif cryptographer == "0":  # Дешифровать
        decrypted_text = decrypt(text_1)
        with open(file, "w", encoding='utf-8') as text:
            text.write(decrypted_text)
            print("Программа успешно выполнена")
        print("Дешифрованное сообщение: ")
        print(decrypted_text)
    else:
        print("Неверно введено. Выберите (0 или 1): ")

except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")


