import math
from itertools import combinations

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

def chebyshev_distance(p1, p2):
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y), abs(p1.z - p2.z))

if __name__ == "__main__":
    points = []
    print("Введите координаты 4 точек в трехмерном пространстве:")
    for i in range(4):
        try:
            x, y, z = map(float, input(f"Точка {i+1} (x y z): ").split())
            points.append(Point3D(x, y, z))
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите три числа, разделенных пробелами.")
            exit()

    print("\nРасстояния между точками:")
    for p1, p2 in combinations(points, 2):
        print(f"Между точками ({p1.x:.2f}, {p1.y:.2f}, {p1.z:.2f}) и ({p2.x:.2f}, {p2.y:.2f}, {p2.z:.2f}):")
        print(f"  Евклидово расстояние: {euclidean_distance(p1, p2):.2f}")
        print(f"  Манхэттенское расстояние: {manhattan_distance(p1, p2):.2f}")
        print(f"  Расстояние Чебышева: {chebyshev_distance(p1, p2):.2f}")
        print()

    print("\nТочки в трехмерном пространстве (координаты):")
    for i, p in enumerate(points):
        print(f"Точка {i+1}: ({p.x:.2f}, {p.y:.2f}, {p.z:.2f})")

    print("\nПримечание: Для отображения точек в трехмерном пространстве графически потребовалось бы использовать специализированные библиотеки или инструменты визуализации (например, matplotlib, Mayavi и т.п.).  В данной программе предоставлены только координаты точек.")
