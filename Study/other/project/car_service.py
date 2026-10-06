# Роль бумаги в графике - играет холст Canvas
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox # tcl/tk
# добавление библиотеки sqlite3
import sqlite3
# создаем переменную для списка
list = []

# считываем sql скрипт
file = open('yzv.db.sql', 'r', encoding='utf8')
build_db = file.read()
file.close()

#создаём соединение с бд
connector = sqlite3.connect("yzv.db")
# слоздаём курсор
cursor = connector.cursor()
# выполнение SQL скрипта по созданиюи запонению БД
cursor.executescript(build_db)
# выбор вех данных из таблицы
sql_services = cursor.execute("Select * from services")

# добавляем каждую новую услугу в список
for row in sql_services:
    list.append(row[1])

# записываем изменения в бд
connector.commit()
#закрываем курсор
cursor.close()
#закрытие соединения (отключекние бд)
connector.close()
class my_combobox:
    def __init__(self,list,font,x,y,width,window):
        self.x = x
        self.y = y
        self.list = list
        self.font = font
        self.width = width
        self.window = window


        # values = self.list -сдержимое списка
        # font = self.font -тип и размер шрифта
        # режим только чтения "readonly"
        self.combobox = Combobox(values=self.list, font=self.font, state="readonly")
        # x = self.x,y = self.y - координаты текстового поля
        # width= self.width - ширина текстового поля
        self.combobox.place(x=self.x, y=self.y, width=self.width)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.select())

    def select(self):
        global price, service
        if self.combobox.get()== self.list[0]:
            self.price = 1500
        elif self.combobox.get()== self.list[1]:
            self.price = 600
        elif self.combobox.get()== self.list[2]:
            self.price = 1300
        elif self.combobox.get() == self.list[3]:
            self.price = 800
        elif self.combobox.get() == self.list[4]:
            self.price = 1200
        elif self.combobox.get() == self.list[5]:
            self.price = 800
        elif self.combobox.get() == self.list[6]:
            self.price = 600
        else:
            self.price = 0
        price= self.price
        service = self.combobox.get()

        self.new_label = my_label("Цена: "+ str(self.price)+"руб.","Arial 15","lightblue",450,200)
        self.combobox = Combobox(values=self.list, font=self.font, state="readonly")
        # x = self.x,y = self.y - координаты текстового поля
        # width= self.width - ширина текстового поля
        self.combobox.place(x=self.x, y=self.y, width=self.width)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.select())

    def select(self):
        global price, service
        if self.combobox.get()== self.list[0]:
            self.price = 1500
        elif self.combobox.get()== self.list[1]:
            self.price = 600
        elif self.combobox.get()== self.list[2]:
            self.price = 1300
        elif self.combobox.get() == self.list[3]:
            self.price = 900
        elif self.combobox.get() == self.list[4]:
            self.price = 2400
        elif self.combobox.get() == self.list[5]:
            self.price = 800
        elif self.combobox.get() == self.list[6]:
            self.price = 600
        else:
            self.price = 0
        price= self.price
        service = self.combobox.get()

        self.new_label = my_label("Цена: " + str(self.price) + "руб.", "Arial 15", "lightblue", 450, 175)
        self.combobox = Combobox(values=self.list, font=self.font, state="readonly")
        # x = self.x,y = self.y - координаты текстового поля
        # width= self.width - ширина текстового поля
        self.combobox.place(x=self.x, y=self.y, width=self.width)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.select())


class my_button:
    def __init__(self, text, font, x, y, width,window):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.width = width
        self.button = Button(text = self.text, font = self.font, command=self.click)
        self.button.place(x=self.x, y = self.y, width = self.width)
        self.window = window

    def click(self):
        self.value_marka = self.window.entry_marka.value.get()  # марка машины
        self.value_model = self.window.entry_model.value.get()  # модель машины
        self.value_color = self.window.entry_color.value.get()  # цвет машины
        self.value_year_build = self.window.entry_year_build.value.get()  # год производства машины
        self.value_number = self.window.entry_number.value.get()
        self.print_file()
        messagebox.showinfo("Сообщение","Данные успешно загружены")

    def print_file(self):
        file = open('new_otchet.txt', 'w', encoding='utf8')
        file.write('Марка машины:' + self.value_marka + '\n')
        file.write('Модель машины:' + self.value_model + '\n')
        file.write('Цвет машины:' + self.value_color + '\n')
        file.write('Год производства машины:' + self.value_year_build + '\n')
        file.write('Номер машины:' + self.value_number + '\n')
        file.close()
class my_entry:
    def __init__(self, font, x, y, width):
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.value = StringVar()

        self.entry = Entry(textvariable=self.value, font=self.font)
        self.entry.place(x=self.x, y=self.y, width=self.width)
class my_label:
    def __init__(self, text, font, color, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.label = Label(text = self.text,font = self.font,bg = color)
        self.label.place(x = self.x, y = self.y)
class my_window:
    def __init__(self):
        self.window = Tk()
        # размер
        self.window.geometry('800x800')
        # заголовок
        self.window.title('Моё окно')
        # цвет фона
        self.window.configure(bg='grey')
        # фиксация размера
        self.window.resizable(width = False, height = False)
        # вызов метода для отрисовки
        self.__my_canva()
        # прикрепление надписей
        self.__new_label()
        # прикрепление текстовых полей
        self.__new_entry()
        #прикрепление кноок
        self.__new_button()
        # метод для отрисовки выпаающего спискак
        self.__new_combobox()

        self.__new_combobox()
        # для появления окна используем метод .mainloop
        self.window.mainloop()

    def __my_canva(self):
        # создание канвы
        self.canva = Canvas(width = 900, height = 900, bg = 'blue')
        # прикрепление канвы
        # для размещения объектов - pack - размещает виджеты по горизонтали и вертикали
        self.canva.pack()

    #def __my_canva(self):
        self.canva = Canvas(width=800, height=800, bg='white')
        self.canva.pack()

    def __new_label(self):
        self.label_title = my_label("АВТОСЕРВИС <Какие Люди!!>", "Arial 20","lightblue", 180,50)
        self.label_marka = my_label("Марка автомобиля:   ", "Arial 15", "lightblue",50,150)
        self.label_model = my_label("Модель автомобиля: ", "Arial 15", "lightblue", 50, 200)
        self.label_color = my_label("Цвет автомобиля:     ", "Arial 15", "lightblue", 50, 250)
        self.year_build = my_label("Год производства:    ", "Arial 15", "lightblue", 50, 300)
        self.car_number = my_label("Номер автомобиля:   ", "Arial 15", "lightblue", 50, 350)
        self.service_combobox = my_label("Услуги для вашей малышки)","Arial 15","lightblue",450,100)
        self.service_combo = my_label("Тюнинг для вашей малышки)", "Arial 15", "lightblue", 450, 250)

        self.surname = my_label("Фамилия:                   ", "Arial 15", "lightblue", 50, 450)
        self.name = my_label("Имя:                          ", "Arial 15", "lightblue", 50, 500)
        self.phone_number = my_label("Номер телефона      :", "Arial 15", "lightblue", 50, 550)
    def __new_entry(self):
        self.entry_marka = my_entry("Arial 15",270,150,150)
        self.entry_model = my_entry("Arial 15", 270, 200, 150)
        self.entry_color = my_entry("Arial 15", 270, 250, 150)
        self.entry_year_build = my_entry("Arial 15", 270, 300, 150)
        self.entry_number = my_entry("Arial 15", 270, 350, 150)

        self.entry_surname = my_entry("Arial 15", 270, 450, 150)
        self.entry_name = my_entry("Arial 15", 270, 500, 150)
        self.entry_phone_number = my_entry("Arial 15", 270, 550, 150)

    def __new_button(self):
        self.write_btn = my_button("Записать","Arial 15",500,600,100,self)
    # ниже метод для отрисовки выпадающего списка
    def __new_combobox(self):
        self.list = [
            "Улучшение двигателя","Крафт"
        ]
        self.service_combobox = my_combobox (self.list,"Arial 13",450,400,200,self)
    def __new_combobox(self):
        global list
        self.service_combobox = my_combobox(list,"Arial 13",450,150,200,self)
# создаем экземпляр класса
new_window = my_window()
