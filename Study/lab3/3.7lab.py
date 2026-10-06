import random
import string
def generate_password(length, uppercase, lowercase, numbers, special):
    # Собираем символы для пароля
    characters = ""
    if uppercase:  # Заглавные буквы
        characters += string.ascii_uppercase  # Если пользователь вводит "да", добавляем все заглавные буквы
    if lowercase:  # Строчные буквы
        characters += string.ascii_lowercase
    if numbers:  # Цифры
        characters += string.digits
    if special:  # Специальные символы
        characters += string.punctuation

    # Если не выбран ни один тип символов, возвращаем None
    if not characters:  # Пользователь ничего не выбрал
        return None

    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Присваивается password


def main():  # Функция, которая будет взаимодействовать с пользователем
    length = int(input("Введите желаемую длину пароля (целое число): "))
    uppercase = input("Нужны ли заглавные буквы (да/нет)? ").strip().lower() == 'да'
    lowercase = input("Нужны ли строчные буквы (да/нет)? ").strip().lower() == 'да'
    numbers = input("Нужны ли цифры (да/нет)? ").strip().lower() == 'да'
    special = input("Нужны ли специальные символы (да/нет)? ").strip().lower() == 'да'
    #.strip() убирает пробелы lower() в нижний регистр
    # Генерация пароля по параметрам
    password = generate_password(length, uppercase, lowercase, numbers, special)

    if password:  # Проверка пароля
        print("Сгенерированный пароль: ", password)
    else:
        print("Ошибка: Не выбрано ни одного типа символов для пароля.")

if __name__ == "__main__":#без этого программа не запуститься
    main()
