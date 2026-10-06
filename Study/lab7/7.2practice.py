#Повторы в тексте
#C:/Users/~Darr_Kness~/Downloads/lab10/file1.txt
a=input("Введите путь к файлу:")
try:
    with open(a, 'r', encoding='utf-8') as f:
        text = f.readline()
except FileNotFoundError:
    print("Файл не найден.")
    exit()
print(text)
