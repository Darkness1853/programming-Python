#C:/Users/~Darr_Kness~/Downloads/lab10/file1.txt
a=input("Введите путь к файлу:")
try:
    with open(a, 'r', encoding='utf-8') as f:
        record = f.readline()
except FileNotFoundError:
    print("Файл не найден.")
    exit()
max_score = 0
winner=""
for t in f:
    t=t.split()
    if int(t[-1])>max_score:
        winner = t[0]+" "+t[1]
        max_score = int(t[-1])
# t=record.split()
# while record:
#     if int(t[-1])>max_score:
#         winner=t[0]+" "+t[1]
#         max_score=int(t[-1])
#         record = f.readline()
# print(winner)