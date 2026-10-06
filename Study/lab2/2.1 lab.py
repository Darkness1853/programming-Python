t= input("Введите товар:")
cost = float(input("Введите стоимость товара: "))

if t == "шорты" or t == "сланцы" or t == "кепка":
    if cost >1000:
        print("цена:",cost, "\nскидка:10% \nцена со скидкой :",cost - cost*0.1)
    elif cost >2000:
        print("цена:", cost, "\nскидка:15% \nцена со скидкой :", cost - cost * 0.15)
    else:
        print("цена:",cost)
else:
    print("цена:",cost)
