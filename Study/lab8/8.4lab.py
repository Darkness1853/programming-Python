import tkinter as tk
import random
from PIL import Image, ImageTk
import winsound

# Воспроизведение звука
winsound.PlaySound("C:/Users/~Darr_Kness~/Downloads/the_matrix_02-Spybreak-_Short-One_.wav",
                   winsound.SND_FILENAME | winsound.SND_ASYNC)

def generate_random_number():
    try:
        lower_bound = int(entry_low.get())
        upper_bound = int(entry_high.get())
        if lower_bound >= upper_bound:
            result_label.config(text="Ошибка: нижняя граница рандома должна быть меньше верхней.")
        else:
            random_number = random.randint(lower_bound, upper_bound)
            result_label.config(text=f"Сгенерированное число: {random_number}")
    except ValueError:
        result_label.config(text="Ошибка: введите корректные целые числа.")

root = tk.Tk()
root.title("Рандом :3")
root.configure(bg='lightblue')
root.geometry("300x300")
canvas = tk.Canvas(root, bg='lightblue')
canvas.pack()

gif_image = Image.open("C:/Users/~Darr_Kness~/Downloads/58aea8b59bfa8c3df11f18d9093ed528.gif")
frames = []

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

# Поля для ввода границ
label_low = tk.Label(root, text="Нижняя граница:", bg='lightgreen', fg='black')
label_low.pack()

entry_low = tk.Entry(root)
entry_low.pack()

label_high = tk.Label(root, text="Верхняя граница:", bg='lightgreen', fg='black')
label_high.pack()

entry_high = tk.Entry(root)
entry_high.pack()

# Кнопка для генерации числа
generate_button = tk.Button(root, text="Сгенерировать", command=generate_random_number, bg='orange', fg='black')
generate_button.pack()

# вывод результата
result_label = tk.Label(root, text="", bg='lightblue', fg='black')
result_label.pack()

# Запуск
root.mainloop()