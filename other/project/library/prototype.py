with open("library.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
def add_book():
    try:
        name = input("Введите название книги: ")
        author = input("Введите автора: ")
        cnt = int(input("Введите количество книг: "))
        new_entry = f"{name};{author};{cnt}\n"

        if new_entry.strip() not in lines:
            lines.append(new_entry)
            save_books()
            print("Книга успешно добавлена.")
        else:
            print("Такая книга уже существует.")
    except ValueError:
        print("Пожалуйста, введите корректное количество книг (число).")

def delete_book():
    try:
        print("Введите данные, чтобы удалить книгу.")
        name = input("Введите название книги: ").strip()
        author = input("Введите автора: ").strip()
        cnt = int(input("Введите количество книг: "))
        entry_to_remove = f"{name};{author};{cnt}"

        if entry_to_remove in lines:
            lines.remove(entry_to_remove)
            save_books()
            print("Книга успешно удалена.")
        else:
            print("Книга не найдена.")
    except ValueError:
        print("Пожалуйста, введите корректное количество книг (число).")

def catalog():
    print("Каталог книг:")
    for line in lines:
        print(line.strip())

def save_books():
    with open("library.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

while True:
    try:
        number = int(input("Введите цифру чтобы взаимодействовать с библиотекой.\nВведи(0) чтобы открыть каталог.\nВведи(1) чтобы добавить книгу.\nВведи(2) чтобы удалить книгу.\nВведи(3) чтобы уйти.\nВаш выбор: "))

        if number == 0:
            catalog()
        elif number == 1:
            add_book()
        elif number == 2:
            delete_book()
        elif number == 3:
            print("Спасибо за то, что воспользовались нашей программой.")
            exit(0)
        else:
            print("Введите значение в диапазоне от 0 до 3.")
    except ValueError:
        print("Введите правильные значения, не буквы!")
