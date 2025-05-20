# Исходный файл
# Ссылка на GitHub пользователя: https://github.com/Srgusev/Calculate/blob/6b780a2082d5810d7c39d7940375a15b9d6b7d55/Calculate%20v.2/Calculate/Calculate.py
# Ссылка на материал: https://habr.com/ru/companies/otus/articles/481806/
from tkinter import *

# Окно
window = Tk()
window.title("CALCULATE")
window.geometry('200x200')
window.resizable(width=False, height=False)

txt = Entry(window, width=20)
txt.place(x=20, y=5)


# очистка окна
def clck(number):
    cur = txt.get()
    txt.delete(0, END)
    txt.insert(0, str(cur) + str(number))


def clear():
    txt.delete(0, END)


def add():
    f_number = txt.get()
    global f_num
    global math
    math = "addition"
    f_num = int(f_number)
    txt.delete(0, END)


def multiply():
    f_number = txt.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(f_number)
    txt.delete(0, END)


def minus():
    f_number = txt.get()
    global f_num
    global math
    math = "minus"
    f_num = int(f_number)
    txt.delete(0, END)


def devide():
    f_number = txt.get()
    global f_num
    global math
    math = "division"
    f_num = int(f_number)
    txt.delete(0, END)


def equal():
    s_number = txt.get()
    txt.delete(0, END)

    if math == "addition":
        txt.insert(0, f_num + int(s_number))
    if math == "minus":
        txt.insert(0, f_num - int(s_number))
    if math == "multiplication":
        txt.insert(0, f_num * int(s_number))
    if math == "division":
        txt.insert(0, f_num / int(s_number))

        # кнопки


btn_1 = Button(window, width=3, height=1, text="1", bg="#fff", font=200, command=lambda: clck(1))
btn_1.place(x=12, y=34)
btn_2 = Button(window, width=3, height=1, text="2", bg="#fff", font=200, command=lambda: clck(2))
btn_2.place(x=55, y=34)
btn_3 = Button(window, width=3, height=1, text="3", bg="#fff", font=200, command=lambda: clck(3))
btn_3.place(x=99, y=34)
btn_4 = Button(window, width=3, height=1, text="4", bg="#fff", font=200, command=lambda: clck(4))
btn_4.place(x=12, y=70)
btn_5 = Button(window, width=3, height=1, text="5", bg="#fff", font=200, command=lambda: clck(5))
btn_5.place(x=55, y=70)
btn_6 = Button(window, width=3, height=1, text="6", bg="#fff", font=200, command=lambda: clck(6))
btn_6.place(x=99, y=70)
btn_7 = Button(window, width=3, height=1, text="7", bg="#fff", font=200, command=lambda: clck(7))
btn_7.place(x=12, y=105)
btn_8 = Button(window, width=3, height=1, text="8", bg="#fff", font=200, command=lambda: clck(8))
btn_8.place(x=55, y=105)
btn_9 = Button(window, width=3, height=1, text="9", bg="#fff", font=200, command=lambda: clck(9))
btn_9.place(x=99, y=105)
btn_e = Button(window, width=3, height=1, text="=", bg="#fff", font=200, command=equal)
btn_e.place(x=12, y=140)
btn_0 = Button(window, width=3, height=1, text="0", bg="#fff", font=200, command=lambda: clck(0))
btn_0.place(x=55, y=140)
btn_c = Button(window, width=3, height=1, text="c", bg="#fff", font=200, command=clear)
btn_c.place(x=99, y=140)
btn_add = Button(window, width=3, height=1, text="+", bg="#fff", font=200, command=add)
btn_add.place(x=140, y=34)
btn_min = Button(window, width=3, height=1, text="-", bg="#fff", font=200, command=minus)
btn_min.place(x=140, y=70)
btn_um = Button(window, width=3, height=1, text="x", bg="#fff", font=200, command=multiply)
btn_um.place(x=140, y=105)
btn_rd = Button(window, width=3, height=1, text="/", bg="#fff", font=200, command=devide)
btn_rd.place(x=140, y=140)

window.mainloop()
