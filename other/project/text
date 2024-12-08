from art import *
from PIL import Image

# Здесь вы можете использовать любое изображение аниме девушки.
# Замените 'anime_girl.jpg' на путь к вашему изображению.
image_path = 'anime_girl.jpg'

# Параметры для преобразования
width = 100  # Ширина ASCII-арт
height = 100  # Высота ASCII-арт

# Открытие изображения и преобразование его в ASCII
img = Image.open(image_path)
img = img.resize((width, height))
img = img.convert('L')  # Конвертация в градации серого

# Определение символов для представления градаций серого
ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

ascii_art = pixel_to_ascii(img)

# Форматирование строки для вывода
img_width, img_height = img.size
ascii_art_lines = [ascii_art[i:i + img_width] for i in range(0, len(ascii_art), img_width)]

# Вывод результата
for line in ascii_art_lines:
    print(line)