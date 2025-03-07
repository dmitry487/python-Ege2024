import math

def calculator(x, y, operation):
    """
    Вычисляет результат операции над двумя числами.
    """
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return "Деление на ноль!"  
        return x / y
    else:
        return "Неизвестная операция"

def advanced_calculator(x, y):
  """Вычисляет дополнительные функции."""
  results = {
      "e^(x+y)": math.exp(x + y),
      "sin(x+y)": math.sin(x + y),
      "cos(x+y)": math.cos(x + y),
      "xy": x * y
  }
  return results



x = float(input("Введите первое число (x): "))
y = float(input("Введите второе число (y): "))
op = input("Введите операцию (+, -, *, /): ")

result = calculator(x, y, op)
print(f"Результат операции {op}: {result}")


advanced_results = advanced_calculator(x,y)
print("\nДополнительные результаты:")
for func_name, result in advanced_results.items():
    print(f"{func_name}: {result:.4f}")

