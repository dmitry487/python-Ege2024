import numpy as np
import matplotlib.pyplot as plt
import math


def my_function(x):
    return (np.sqrt(1 + np.exp(np.sqrt(x))) + np.cos(x**2)) / abs(1 - np.sin(x)**3) + np.log(abs(2*x))


x_values = np.linspace(1, 10, 10) 
y_values = np.array([my_function(x) for x in x_values])

x_slice = x_values[:5]
y_slice = y_values[:5]


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1) 
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue', label='Основной массив')
plt.title('График функции (plt.plot)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()


plt.subplot(1, 2, 2) 
plt.scatter(x_slice, y_slice, color='red', label='Срез первой половины')
plt.title('Точечный график среза (plt.scatter)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.tight_layout() 
plt.show()
