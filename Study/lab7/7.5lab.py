# Дан текстовый файл (можно самим создать). Пользователь вводит новую строку текста. Напишите
#  программу для добавления в середину файла введенной пользователем строки, сохраняя при этом
#  старое содержимое файла.
# C:/Users/~Darr_Kness~/Downloads/lab10/file6.txt
from colorama import Fore
print("Программа которая добавляет текст в середину файла.")
file=input("Введите путь к файлу: ")
str =input("Введите предложение: ")
words=0
my_list=[]
try:
    with open(file,"r",encoding='utf-8') as text:
        my_list = text.readlines()  # Читаем все строки в список
        words_index = len(my_list) // 2
        # Вставляем строку в середину списка
        my_list.insert(words_index, str )
        # Записываем обратно в файл с изменениями
        with open(file, "w", encoding='utf-8') as text:
            text.writelines(my_list)
            print("Программа успешно выполнена")
except FileNotFoundError:
    print("Файл не найден. Пожалуйста, проверьте путь.")
