x = float(input("Введите число x: "))

if x < -5:
  print("Интервал (-∞, -5)")
elif -5 <= x <= 5:
  print("Интервал [-5, 5]")
else:
  print("Интервал (5, +∞)")

