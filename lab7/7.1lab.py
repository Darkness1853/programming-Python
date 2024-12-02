#C:/Users/~Darr_Kness~/Downloads/lab10/file4.txt
a = input("Введите путь к файлу:")
try:
    with open(a, 'r', encoding='utf-8') as f:
        max_score = 0
        score_1 =0
        score_2 =0
        winner = ""
        second_place =""
        third_place =""
        for t in f:
            t = t.split()
            score = int(t[-1])
            if score > max_score:
                winner = t[0] + " " + t[1]
                max_score = score
            elif score > score_1:
                second_place = t[0] + " " + t[1]
                score_1 = score
            elif score > score_2:
                third_place = t[0] + " " + t[1]
                score_2 = score

    if winner :
        print(f"Победитель: {winner} с максимальным счетом: {max_score}")
        if second_place:
            print(f"Призёр: {second_place} со счетом: {score_1}, 2-е место")
        if third_place:
            print(f"Призёр: {third_place} со счетом: {score_2}, 3-е место")
    else:
        print("Нет записей для обработки.")
#Ошибка возникает, когда программа пытается открыть файл, который не существует
except FileNotFoundError:
    print("Файл не найден.")
#Ошибка появляется когда операция получает аргумент правильного типа, но с некорректным значением.
except ValueError:
    print("Ошибка преобразования данных.")