import matplotlib.pyplot as plt
import numpy as np

# размер матрицы: {потоки: время в мс}
data = {
    0: {1: 0, 2: 0, 4: 0, 8: 0, 16: 0},
    200: {1: 11.31, 2: 5.967, 4: 3.208, 8: 3.158, 16: 2.725},
    400: {1: 101.72, 2: 46.767, 4: 36.841, 8: 27.423, 16: 26.923},
    800: {1: 794.9, 2: 477.1, 4: 350.11, 8: 210.78, 16: 196.28},
    1600: {1: 7798.94, 2: 4440.43, 4: 2920.44, 8: 1766.45, 16: 1738.32},
    2000: {1: 19181.07, 2: 11622.66, 4: 6465.06, 8: 3783.13, 16: 3620.15}
}

colors = plt.cm.viridis(np.linspace(0, 1, len(data[200])))
thread_colors = {t: colors[i] for i, t in enumerate(sorted(data[200].keys()))}

plt.figure(figsize=(12, 8))

# Построение графиков
for thread in sorted(data[200].keys()):
    sizes = []
    times = []
    for size in sorted(data.keys()):
        sizes.append(size)
        times.append(data[size][thread])
    plt.plot(sizes, times,
             label=f'{thread} потоков',
             linewidth=2.5,
             color=thread_colors[thread])

# Настройка осей и легенды
plt.title('Зависимость времени выполнения от размера матрицы\nи количества потоков',
          fontsize=14, pad=20)
plt.xlabel('Размер матрицы (N×N)', fontsize=12)
plt.ylabel('Время выполнения (мс)', fontsize=12)

# Установка явных меток на осях (убрали логарифмический масштаб)
plt.xticks(sorted(data.keys()), labels=[str(s) for s in sorted(data.keys())])
plt.yticks(
    [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000],
    labels=['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20']
)
plt.ylim(0, 20000)

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(title='Количество потоков',
           bbox_to_anchor=(1.05, 1),
           loc='upper left',
           fontsize=10)

plt.tight_layout()
plt.show()
