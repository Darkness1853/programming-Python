
import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def f(x):
    return (x**2 + 768) / (x - 16)

# Определяем диапазон значений x
x_values = np.linspace(0, 64, 1000)  # 1000 точек от 0 до 64

# Вычисляем значения функции, избегая точки x=16
y_values = f(x_values)

# Убираем значения в точке асимптоты (x = 16)
y_values[x_values == 16] = np.nan  # Заменяем на NaN, чтобы не отображать на графике

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='y = (x^2 + 768) / (x - 16)', color='blue')
plt.axvline(x=16, color='red', linestyle='--', label='Вертикальная асимптота x=16')
plt.xlim(0, 64)
plt.ylim(-100, 150)  # Установим пределы оси Y для более наглядного отображения
plt.title('График функции y = (x^2 + 768) / (x - 16)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.show()
