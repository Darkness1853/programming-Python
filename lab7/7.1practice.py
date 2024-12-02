# Открытие файла с обработкой ошибок
try:
    with open("C:/Users/~Darr_Kness~/Downloads/lab10/file1.txt", 'r', encoding='utf-8') as f:
        text = f.readline()
except FileNotFoundError:
    print("Файл не найден.")
    exit()

# Вывод текста из файла
print("Текст из файла:", text)

# Символы для удаления
sim = "x,()-!"
for s in sim:
    text = text.replace(s, "")

# Разделение текста на слова
words = text.split()
print("Слова:", *words)

# Поиск самого длинного слова
long_word = max(words, key=len)
print("Самое длинное слово:", long_word)

# Поиск самого короткого слова
short_word = min(words, key=len)
print("Самое короткое слово:", short_word)

# Замена "Все" на "все" и удаление вхождений
words = [word if word.lower() != "все" else "все" for word in words]
print("Слова после изменения 'Все' на 'все':", *words)

# Удаление всех вхождений "все"
words = [word for word in words if word != "все"]
print("Слова после удаления 'все':", *words)