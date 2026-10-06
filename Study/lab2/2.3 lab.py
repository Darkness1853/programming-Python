n = int(input("Введите количество человек: "))
cost = 0

for _ in range(n):  # Цикл до n человек
    age = int(input("Сколько лет: "))
    if age == 0:
        break
    if age <= 2:
        cost += 0
    elif 3 <= age <= 12:
        cost += 100
    elif age > 65:
        cost += 120
    else:
        cost += 200

print("Итоговая стоимость билета:", cost)