import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42) 
array_size = 100
random_array = np.random.rand(array_size)


mean_value = np.mean(random_array)


median_value = np.median(random_array)


print(f"Среднее значение: {mean_value:.4f}")
print(f"Медианное значение: {median_value:.4f}")





plt.figure(figsize=(8, 6))
plt.scatter(range(array_size), random_array, marker='o', s=20) 
plt.xlabel("Индекс")
plt.ylabel("Случайное значение")
plt.title("Точечная диаграмма рассеяния случайных чисел")
plt.grid(True)
plt.show()
