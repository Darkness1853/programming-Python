import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import winsound

# Воспроизведение звука
winsound.PlaySound("C:/Users/~Darr_Kness~/Downloads/the_matrix_02-Spybreak-_Short-One_.wav",
                   winsound.SND_FILENAME | winsound.SND_ASYNC)
root = tk.Tk()
#Установим иконку
icon = PhotoImage(file = "C:/Users/~Darr_Kness~/Downloads/images.png")
root.iconphoto(False, icon)
root.title("Рандом :3")
root.configure(bg='lightblue')
root.geometry("300x300")
canvas = tk.Canvas(root, bg='lightblue')
canvas.pack()

gif_image = Image.open("C:/Users/~Darr_Kness~/Downloads/yakubovich.gif")
frames = []
def assessment():
    points_dict = {
        "1": "A,E,I,L,N,O,R,S,T,U",
        "2": "D,G",
        "3": "B,C,M",
        "4": "F,H,V,W,Y",
        "5": "K",
        "8": "J,X",
        "10": "Q,Z",
    }

    # Ввод слова от пользователя
    word = (entry_low.get()).upper()
    total_points = 0
    for letter in word:
        for points, letters in points_dict.items():
            if letter in letters.split(","):
                total_points += int(points)
    result_label.config(text=f"Сумма полученных баллов: {total_points}")

try:
    while True:
        # Создание кадра и добавление в список
        frame = ImageTk.PhotoImage(gif_image)
        frames.append(frame)
        gif_image.seek(len(frames))  # Переход к следующему кадру
except EOFError:
    pass

label_gif = tk.Label(canvas)
label_gif.pack()

def update_gif(frame_index=0):
    label_gif.config(image=frames[frame_index])
    frame_index += 1
    if frame_index >= len(frames):
        frame_index = 0
    root.after(100, update_gif, frame_index)
# Начинаем обновление GIF
update_gif()
label_low = tk.Label(root, text="Введи слово-> получи балл: ", bg='lightgreen', fg='black')
label_low.pack()

entry_low = tk.Entry(root)
entry_low.pack()

generate_button = tk.Button(root, text="Результат ", command=assessment, bg='orange', fg='black')
generate_button.pack()

# вывод результата
result_label = tk.Label(root, text="", bg='lightblue', fg='black')
result_label.pack()
root.mainloop()